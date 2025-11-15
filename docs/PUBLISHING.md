# Publishing

## PyPI (optional)
1. Ensure version is updated in `pyproject.toml` and `src/spoon_diversity/__init__.py`
2. Build:
   ```bash
   python -m build
   ```
3. Upload (requires credentials):
   ```bash
   python -m pip install twine
   twine upload dist/*
   ```

## Install via pipx
```bash
pipx install spoon-diversity-tools
spoon-diversity --version
```


