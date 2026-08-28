# company-system部署记录

服务器:

Alibaba Cloud Linux 3

资源:

2C 2G 40G


部署组件:

Nginx
Backend
MySQL8
Redis


部署时间:

2026-08-20


备注:

首次部署
# Company System部署文档


## 环境

OS:
Alibaba Cloud Linux 3

Docker:
26.x

Docker Compose:
2.x


## 项目启动


进入目录:

cd /opt/company-app/company-system


启动:

docker compose up -d



## 查看状态


docker ps



## 服务访问


Nginx:

http://服务器IP


接口:

/api/user



## 停止服务


docker compose down



## 重启服务


docker compose restart
