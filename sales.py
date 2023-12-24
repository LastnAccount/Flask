from flask import Flask, make_response, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "37707"
app.config["MYSQL_DB"] = "trytry"

mysql = MySQL(app)

def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return data


@app.route("/sales", methods=["GET"])
def get_sales():
    data = data_fetch("""SELECT * FROM trytry.sales""")
    return make_response(jsonify(data), 200)


@app.route("/sales/<int:id>", methods=["GET"])
def get_sales_by_id(id):
    data = data_fetch("""SELECT * FROM sales where sale_id = {}""".format(id))
    return make_response(jsonify(data), 200)

@app.route("/store/<int:id>", methods=["GET"])
def get_store_by_id(id):
    data = data_fetch("""SELECT * FROM sales where store_id = {}""".format(id))
    return make_response(jsonify(data), 200)

@app.route("/sales", methods=["POST"])
def add_sales():
    cur = mysql.connection.cursor()
    info = request.get_json()
    sales_date_time = info["sales_date_time"]
    total_ammount_due = info["total_ammount_due"]
    cur.execute(
        """ INSERT INTO sales (sales_date_time, total_ammount_due) VALUE (%s, %s)""",
        (sales_date_time, total_ammount_due),
    )
    mysql.connection.commit()
    print("row(s) affected :{}".format(cur.rowcount))
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "New sales added successfully", "rows_affected": rows_affected}
        ),
        201,
    )

@app.route("/sales/<int:id>", methods=["PUT"])
def update_actor(id):
    cur = mysql.connection.cursor()
    info = request.get_json()
    sales_date_time = info["sales_date_time"]
    total_ammount_due = info["total_ammount_due"]
    cur.execute(
        """ INSERT INTO sales (sales_date_time, total_ammount_due) VALUE (%s, %s)""",
        (sales_date_time, total_ammount_due),
    )
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "sales updated successfully", "rows_affected": rows_affected}
        ),
        200,
    )


@app.route("/sales/<int:id>", methods=["DELETE"])
def delete_actor(id):
    cur = mysql.connection.cursor()
    cur.execute(""" DELETE FROM sales where company_id = %s """, (id,))
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "sales deleted successfully", "rows_affected": rows_affected}
        ),
        200,
    )


if __name__ == "__main__":
    app.run(debug=True)
