#!/usr/bin/env bash

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
alembic upgrade head