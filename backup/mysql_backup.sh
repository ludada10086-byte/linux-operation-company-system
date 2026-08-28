#!/bin/bash

set -euo pipefail

PROJECT_DIR="/opt/company-app/company-system"
BACKUP_DIR="${PROJECT_DIR}/backup/mysql"

CONTAINER_NAME="company-mysql"
DATABASE="${MYSQL_DATABASE:-company}"
RETENTION_DAYS="${RETENTION_DAYS:-7}"

DATE=$(date +%Y-%m-%d_%H-%M-%S)
BACKUP_FILE="${BACKUP_DIR}/${DATABASE}_${DATE}.sql"

mkdir -p "${BACKUP_DIR}"

if [ -z "${MYSQL_ROOT_PASSWORD:-}" ]; then
    echo "ERROR: MYSQL_ROOT_PASSWORD is not set"
    exit 1
fi

echo "[$(date '+%F %T')] backup started"

docker exec -e MYSQL_PWD="${MYSQL_ROOT_PASSWORD}" \
    "${CONTAINER_NAME}" \
    mysqldump \
    -uroot \
    --single-transaction \
    --routines \
    --triggers \
    --events \
    --databases "${DATABASE}" \
    > "${BACKUP_FILE}"

if [ ! -s "${BACKUP_FILE}" ]; then
    echo "ERROR: backup file is empty"
    rm -f "${BACKUP_FILE}"
    exit 1
fi

find "${BACKUP_DIR}" \
    -type f \
    -name "*.sql" \
    -mtime +"${RETENTION_DAYS}" \
    -delete

echo "[$(date '+%F %T')] backup success"
echo "Backup file: ${BACKUP_FILE}"

ls -lh "${BACKUP_FILE}"
