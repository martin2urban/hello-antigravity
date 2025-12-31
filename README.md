# Hello Antigravity

This is a sample Python project created with `Antigravity`. It follows a standard package structure with tests.

## Structure

```
hello_antigravity/
├── src/
│   └── hello_antigravity/
│       ├── __init__.py
│       └── main.py
├── tests/
│   └── test_main.py
├── pyproject.toml
└── README.md
```

## Installation

You can install this package locally in editable mode:

```bash
pip install -e .
```

## Usage

After installation, you can run the script using the command line entry point defined in `pyproject.toml`:

```bash
hello-antigravity
```

Or run the module directly:

```bash
python -m hello_antigravity.main
```

## Testing

Install `pytest` and run the tests:

```bash
pip install pytest
pytest
```
