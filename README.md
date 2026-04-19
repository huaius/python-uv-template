## Usage guide

```bash
uv run my-uv-template 2 3
```

### Preparation
Cusomers need to install following tools to proceed. 

You can install UV in a number of ways including pip install.

```bash
pipx install uv
```

or a curl request and execution

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Once you have it installed confirm the version with

```bash
uv --version
```


## Development guide

### Lint check

```bash
uvx ruff check

uvx ruff check --fix
```

### Build
Run uv build so we can get the packaged up wheel files and ensure that they are also pass linting checks correctly.
```bash
uv build
```

### Test

```bash
pytest -v
python -m pytest -v
```
### Test Coverage

```bash
pytest --cov-report html --cov=my_uv_template tests/
```





## Reference
https://blog.hungovercoders.com/datagriff/2025/08/15/simplify-python-package-development-with-uv-and-taskfile.html


