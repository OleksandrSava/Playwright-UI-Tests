# Playwright UI Tests

Lightweight Playwright (Python) test suite for UI checks — runnable locally, in Docker, and in CI.

## Quick start
1. Clone:
```bash
git clone https://github.com/OleksandrSava/Playwright-UI-Tests.git
cd Playwright-UI-Tests
```
2. Env & deps:
```bash
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
playwright install
```
3. Run tests:
```bash
pytest -q
# specific file:
pytest tests/test_example.py -q
```

## Docker
Build and run:
```bash
docker build -t playwright-ui-tests .
docker run --rm playwright-ui-tests
```

## CI / Notes
- Example GitHub Actions workflow: install deps, `playwright install`, then `pytest`.
- If a push fails when adding `.github/workflows/*`, ensure your auth method (PAT or gh/SSH) has workflow permissions.
