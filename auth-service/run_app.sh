#! /bin/sh

python -m uvicorn src.main:app --host 0.0.0.0 --port 3001 --reload