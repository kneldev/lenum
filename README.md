# lenum

Linux state enumerator proof of concept.

## Project Layout

- `src/lenum/controller.py` - controller that runs selected modules and aggregates results.
- `src/lenum/modules/` - focused enumeration modules.
- `src/lenum/cli.py` - CLI entrypoint for `uv run lenum`.

## Enumeration Contract

Each module exposes a `name` and a `run()` method. `run()` returns a dictionary,
giving the controller one consistent result shape to aggregate before report
generation.
