from flask import Flask, jsonify
import redis
import pymysql
import json


app = Flask(__name__)


redis_client = redis.Redis(
    host="company-redis",
    port=6379,
    decode_responses=True
)


def mysql_conn():

    return pymysql.connect(
        host="company-mysql",
        user="root",
        password="123456",
        database="company",
        charset="utf8"
    )


@app.route("/api/user")
def user():


    # 先查redis

    data = redis_client.get("user")


    if data:

        return jsonify(
            {
                "source":"redis",
                "data":json.loads(data)
            }
        )


    # redis没有，查mysql

    conn=mysql_conn()

    cursor=conn.cursor()

    cursor.execute(
        "select id,name from user_test limit 1"
    )

    result=cursor.fetchone()

    conn.close()


    user_data={
        "id":result[0],
        "name":result[1]
    }


    # 写入redis

    redis_client.set(
        "user",
        json.dumps(user_data)
    )


    return jsonify(
        {
            "source":"mysql",
            "data":user_data
        }
    )



@app.route("/health")
def health():

    return "backend ok"


if __name__=="__main__":

    app.run(
        host="0.0.0.0",
        port=8080
    )
