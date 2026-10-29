# asset-inventory-merger

Merge two CSV asset inventories by serial number, deduplicating and reporting conflicts instead of silently overwriting.

## How to run

```sh
python3 main.py old.csv new.csv
```

## Example output

```
Merged 42 assets, 1 conflict(s).
- conflict on serial SN-1042 (newer file wins)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
