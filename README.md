# lenum

Linux state enumerator proof of concept.

## Project Layout

- `src/lenum/controller.py` - singleton controller that owns module instances.
- `src/lenum/modules/` - focused enumeration modules.
- `src/lenum/cli.py` - CLI entrypoint for `uv run lenum`.
