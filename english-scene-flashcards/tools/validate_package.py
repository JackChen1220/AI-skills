#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, json, re

parser = argparse.ArgumentParser()
parser.add_argument('root', nargs='?', default='.')
parser.add_argument('--strict', action='store_true')
args = parser.parse_args()
root = Path(args.root).resolve()

required_dirs = ['core', 'engine', 'schemas', 'adapters', 'assets', 'tools']
required_files = [
    'SKILL.md', 'AGENT_CONTRACT.md', 'ADAPTER_ROUTING.md', 'PACKAGE_MANIFEST.json',
    'core/workflow.md', 'core/source_truth.md', 'core/grouping_rules.md', 'core/scene_brief_rules.md',
    'core/visual_spec.md', 'core/connector_system_v3.md', 'core/design_tokens.json', 'core/qa_rules.md',
    'engine/README.md', 'engine/state_machine.md', 'engine/prompt_compiler_contract.md',
    'engine/composer_contract.md', 'engine/qa_engine_contract.md', 'engine/artifact_store_contract.md',
    'schemas/vocabulary.schema.json', 'schemas/vocabulary_master.schema.json',
    'schemas/card_plan.schema.json', 'schemas/card_plan_set.schema.json',
    'schemas/scene_brief.schema.json', 'schemas/layout_spec.schema.json',
    'schemas/compiled_prompt.schema.json', 'schemas/base_asset.schema.json',
    'schemas/qa_report.schema.json', 'schemas/repair_action.schema.json',
    'schemas/manifest.schema.json', 'schemas/run_state.schema.json',
    'adapters/generic/ADAPTER_TEMPLATE.md', 'adapters/openai/ADAPTER.md',
    'adapters/doubao_work/ADAPTER.md', 'adapters/qwen_office/ADAPTER.md',
    'assets/golden_set/README.md', 'assets/golden_set/G3A-U01-C01-approved.png'
]

errors = []
for d in required_dirs:
    if not (root / d).is_dir():
        errors.append(f'missing required directory: {d}/')
for f in required_files:
    if not (root / f).is_file():
        errors.append(f'missing required file: {f}')

# Parse every JSON and, in strict mode, validate every JSON Schema against Draft 2020-12.
for p in root.rglob('*.json'):
    try:
        json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:
        errors.append(f'invalid JSON {p.relative_to(root)}: {e}')

if args.strict:
    try:
        from jsonschema import Draft202012Validator
        for p in (root / 'schemas').glob('*.json'):
            try:
                Draft202012Validator.check_schema(json.loads(p.read_text(encoding='utf-8')))
            except Exception as e:
                errors.append(f'invalid JSON Schema {p.relative_to(root)}: {e}')
    except ImportError:
        print('WARNING: jsonschema not installed; meta-schema validation skipped.')

# Manifest inventory integrity.
# Source ZIP packages can enforce bytes/SHA256. GitHub repository distributions rely on Git object
# integrity because reference assets may be intentionally recompressed for repository portability.
# The top-level demo/ gallery is repository-only presentation content and intentionally sits outside
# the distributable Skill package manifest.
mp = root / 'PACKAGE_MANIFEST.json'
if mp.is_file():
    try:
        m = json.loads(mp.read_text(encoding='utf-8'))
        listed = {x['path']: x for x in m.get('files', [])}
        actual = {
            str(p.relative_to(root)).replace('\\', '/')
            for p in root.rglob('*')
            if p.is_file()
            and p.name != 'PACKAGE_MANIFEST.json'
            and not str(p.relative_to(root)).replace('\\', '/').startswith('demo/')
        }
        if set(listed) != actual:
            for x in sorted(actual - set(listed)):
                errors.append(f'unlisted package file: {x}')
            for x in sorted(set(listed) - actual):
                errors.append(f'manifest references missing file: {x}')
        if m.get('file_count_excluding_manifest') != len(actual):
            errors.append(
                f'manifest file_count_excluding_manifest mismatch: '
                f'{m.get("file_count_excluding_manifest")} != {len(actual)}'
            )

        is_git_distribution = 'GitHub repository distribution' in m.get('distribution_note', '')
        if args.strict and not is_git_distribution:
            for rel, item in listed.items():
                p = root / rel
                if not p.is_file():
                    continue
                data = p.read_bytes()
                sha = hashlib.sha256(data).hexdigest()
                if item.get('bytes') != len(data):
                    errors.append(f'byte-size mismatch: {rel}')
                if item.get('sha256') != sha:
                    errors.append(f'sha256 mismatch: {rel}')
        elif args.strict and is_git_distribution:
            print('INFO: GitHub distribution detected; file inventory is checked, while byte/SHA256 '
                  'checks defer to Git object integrity because reference assets may be recompressed.')
    except Exception as e:
        errors.append(f'PACKAGE_MANIFEST.json error: {e}')

# Backtick path references in Markdown.
if args.strict:
    path_re = re.compile(r'`([^`]+)`')
    for md in root.rglob('*.md'):
        txt = md.read_text(encoding='utf-8')
        for ref in path_re.findall(txt):
            if ref.startswith('/mnt/') or ' -> ' in ref or ref.startswith('http'):
                continue
            if ref.endswith('/*.json') or ref == 'schemas/*.json' or ref == 'engine/*.md':
                if not list(root.glob(ref)):
                    errors.append(f'{md.relative_to(root)} unresolved glob reference: {ref}')
            elif any(ref.startswith(prefix) for prefix in ['core/', 'engine/', 'schemas/', 'adapters/', 'assets/', 'tools/']) and (' ' not in ref):
                if not (root / ref).exists():
                    errors.append(f'{md.relative_to(root)} unresolved package reference: {ref}')

# Minimal example schema validation when jsonschema exists.
if args.strict:
    try:
        from jsonschema import Draft202012Validator

        def validate_collection(instance_rel, wrapper_rel, item_rel):
            instance = json.loads((root / instance_rel).read_text(encoding='utf-8'))
            wrapper = json.loads((root / wrapper_rel).read_text(encoding='utf-8'))
            item = json.loads((root / item_rel).read_text(encoding='utf-8'))
            wrapper = dict(wrapper)
            wrapper['items'] = item
            Draft202012Validator(wrapper).validate(instance)

        validate_collection(
            'examples/minimal_run/vocabulary_master.json',
            'schemas/vocabulary_master.schema.json',
            'schemas/vocabulary.schema.json',
        )
        validate_collection(
            'examples/minimal_run/card_plan.json',
            'schemas/card_plan_set.schema.json',
            'schemas/card_plan.schema.json',
        )
    except ImportError:
        pass
    except Exception as e:
        errors.append(f'minimal-run schema validation failed: {e}')

if errors:
    print('PACKAGE VALIDATION: FAIL')
    for e in errors:
        print(' -', e)
    raise SystemExit(1)

print('PACKAGE VALIDATION: PASS')
print('Root:', root)
print(f'Required files: {len(required_files)} / {len(required_files)}')
print(f'JSON schemas: {len(list((root / "schemas").glob("*.json")))} parseable')
print('Strict mode:', 'ON' if args.strict else 'OFF')
