# Company System

基于 Docker Compose 部署的资产管理系统。

项目实现：

- Web服务部署
- 数据库持久化
- Redis缓存
- Nginx反向代理
- Prometheus + Grafana监控
- 自动化备份
- CI/CD自动部署


---

# 项目架构


用户
 |
 |
Nginx
 |
 |
Flask Backend
 |
 +-------------+
 |             |
MySQL        Redis


监控：

Prometheus
 |
 +-- Node Exporter
 |
 +-- cAdvisor

Grafana


---

# 技术栈


## 服务

|组件|版本|
|-|-|
|Linux|Alibaba Cloud Linux 3|
|Docker|26.x|
|Docker Compose|2.x|
|Nginx|latest|
|Python Flask|3.x|
|MySQL|8.0|
|Redis|7.0|


## 监控

- Prometheus
- Grafana
- Node Exporter
- cAdvisor


---

# 功能


## 后端接口

首页:GET /
健康检查:GET /health
用户查询:GET /api/assets
资产查询:GET /api/assets
 
git branch test
