from flask import Flask, jsonify
import redis
import pymysql
import json
import logging
import os


app = Flask(__name__)


# =========================
# 日志配置
# =========================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)


# =========================
# Redis连接
# =========================

redis_client = redis.Redis(
    host="company-redis",
    port=6379,
    decode_responses=True
)


# =========================
# MySQL连接
# =========================

def mysql_conn():

    return pymysql.connect(
        host="company-mysql",
        user="root",
        password=os.environ.get("MYSQL_ROOT_PASSWORD", ""),
        database="company",
        charset="utf8"
    )



# =========================
# 首页
# =========================

@app.route("/")
def index():

    return jsonify(
        {
            "system": "Company Asset Management System",
            "version": "2.0"
        }
    )



# =========================
# 健康检查
# =========================

@app.route("/health")
def health():

    return "backend ok"



# =========================
# 查询资产
# Redis缓存
# MySQL数据源
# =========================

@app.route("/api/assets")
def assets():


    # 1. 查询Redis

    cache = redis_client.get("assets")


    if cache:

        logger.info(
            "assets data from redis"
        )

        return jsonify(
            {
                "source": "redis",
                "data": json.loads(cache)
            }
        )



    # 2. Redis没有数据
    # 查询MySQL

    logger.info(
        "assets data from mysql"
    )


    conn = mysql_conn()

    cursor = conn.cursor()


    cursor.execute(
        """
        select hostname,ip,status
        from assets
        """
    )


    rows = cursor.fetchall()


    conn.close()



    data = []


    for row in rows:

        data.append(
            {
                "hostname": row[0],
                "ip": row[1],
                "status": row[2]
            }
        )



    # 写入Redis缓存

    redis_client.set(
        "assets",
        json.dumps(data)
    )



    return jsonify(
        {
            "source": "mysql",
            "data": data
        }
    )




# =========================
# 查询用户
# =========================

@app.route("/api/users")
def users():


    conn = mysql_conn()

    cursor = conn.cursor()


    cursor.execute(
        """
        select id,name,role
        from users
        """
    )


    rows = cursor.fetchall()


    conn.close()



    data = []


    for row in rows:

        data.append(
            {
                "id": row[0],
                "name": row[1],
                "role": row[2]
            }
        )



    return jsonify(data)




# =========================
# 启动
# =========================

if __name__ == "__main__":


    app.run(
        host="0.0.0.0",
        port=8080
    )
