#!/bin/bash

DATE=$(date +%F_%H-%M-%S)
BACKUP_DIR=/opt/company-app/company-system/backup/mysql

CONTAINER_NAME=company-mysql
DATABASE=company
USER=root
PASSWORD=123456

BACKUP_FILE=${BACKUP_DIR}/${DATABSES}_${DATE}.sql

echo "开始备份数据库..."

docker exec ${CONTAINER_NAME} \
mysqldump \
-u${USER} \
-p${PASSWORD} \
${DATABASE} > ${BACKUP_FILE}


if [ $? -eq 0 ];then
	echo "数据库备份成功"
	ls -lh ${BACKUP_FILE}

else
	echo "数据库备份失败"
	exit 1
fi
