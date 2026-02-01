# fastapi-project

Small FastAPI example project demonstrating request parameters, headers, and cookies.

## Prerequisites

- Python 3.10+
- A virtual environment is recommended

## Install

Windows PowerShell:

```powershell
python -m venv .venv
. .venv/Scripts/Activate.ps1
pip install -r requirements.txt
```

## Run

```powershell
uvicorn main:app --reload --port 8000
```

Open the interactive docs at http://127.0.0.1:8000/docs

## Notable endpoints

- `GET /read-cookies/` — reads individual cookies (`ads_id`, `auth_key`)
- `GET /read-multiple-cookies/` — reads multiple cookies via a Pydantic model
- `GET /read-headers/` — example of reading a `User-Agent` header
- `GET /convert_underscores-disable-headers/` — example with `convert_underscores=False`
- `GET /duplicate-headers/` — reads duplicate header values into a list
- `GET /multiple-headers/` — reads multiple headers into a Pydantic model

## Notes

- `main.py` contains many commented example routes illustrating FastAPI features.
- The `POST /user` handler in `main.py` appears to be a placeholder and may need implementation or cleanup.

## Files

- [main.py](main.py)
- [requirements.txt](requirements.txt)
- [Practice/cookies.py](Practice/cookies.py)
- [Practice/HeaderParameters.py](Practice/HeaderParameters.py)
