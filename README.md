# lenum

Linux state enumerator proof of concept.

## Project Layout

- `src/lenum/controller.py` - controller that runs selected modules and aggregates results.
- `src/lenum/models.py` - shared dataclasses used by modules, aggregation, and reports.
- `src/lenum/modules/` - focused enumeration modules.
- `src/lenum/cli.py` - CLI entrypoint for `uv run lenum`.

## Enumeration Contract

Each module exposes a `name` and a `run()` method. `run()` returns a `ModuleResult`
from `lenum.models`, giving the controller one consistent result shape to
aggregate before report generation.
