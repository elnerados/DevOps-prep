# docker-lab

Cvičná FE/BE/DB aplikace z přípravy na DevOps pozici.

## Stack
- **backend** — FastAPI (Python), čte/píše do PostgreSQL
- **db** — PostgreSQL 16 s persistent volume
- **proxy** — nginx jako reverse proxy

## Spuštění
```bash
docker compose up -d --build
```

## Endpointy
- `GET /` — uvítací zpráva
- `GET /health` — health check
- `GET /api/time` — aktuální čas
- `POST /api/visit` — zapíše návštěvu do DB
- `GET /api/visits` — vypíše návštěvy z DB

## Vývoj

Lokálně:
```bash
docker compose up -d --build
```
