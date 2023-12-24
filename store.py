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


@app.route("/stores", methods=["GET"])
def get_stores():
    data = data_fetch("""SELECT * FROM trytry.stores""")
    return make_response(jsonify(data), 200)


@app.route("/stores/<int:id>", methods=["GET"])
def get_stores_by_id(id):
    data = data_fetch("""SELECT * FROM stores where sale_id = {}""".format(id))
    return make_response(jsonify(data), 200)

@app.route("/stores", methods=["POST"])
def add_stores():
    cur = mysql.connection.cursor()
    info = request.get_json()
    store_name = info["store_name"]
    store_address = info["store_address"]
    other_store_details = info["other_store_details"]
    cur.execute(
        """ INSERT INTO stores (store_name, store_address, other_store_details) VALUE (%s, %s, %s)""",
        (store_name, store_address, other_store_details),
    )
    mysql.connection.commit()
    print("row(s) affected :{}".format(cur.rowcount))
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "New stores added successfully", "rows_affected": rows_affected}
        ),
        201,
    )

@app.route("/stores/<int:id>", methods=["PUT"])
def update_stores(id):
    cur = mysql.connection.cursor()
    info = request.get_json()
    store_name = info["store_name"]
    store_address = info["store_address"]
    other_store_details = info["other_store_details"]
    cur.execute(
        """ INSERT INTO stores (store_name, store_address, other_store_details) VALUE (%s, %s, %s)""",
        (store_name, store_address, other_store_details),
    )
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "stores updated successfully", "rows_affected": rows_affected}
        ),
        200,
    )


@app.route("/stores/<int:id>", methods=["DELETE"])
def delete_stores(id):
    cur = mysql.connection.cursor()
    cur.execute(""" DELETE FROM stores where sale_id = %s """, (id,))
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "stores deleted successfully", "rows_affected": rows_affected}
        ),
        200,
    )


if __name__ == "__main__":
    app.run(debug=True)
