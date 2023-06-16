#! /bin/sh

set -ex

#export DATABASE_URL="postgresql+asyncpg://postgres:postgres@localhost:5432/blogger_user_service"
python -m uvicorn src.main:app --host 0.0.0.0 --port 3002 --reload