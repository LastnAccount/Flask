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


@app.route("/company", methods=["GET"])
def get_company():
    data = data_fetch("""SELECT * FROM trytry.companies""")
    return make_response(jsonify(data), 200)


@app.route("/company/<int:id>", methods=["GET"])
def get_company_by_id(id):
    data = data_fetch("""SELECT * FROM companies where company_id = {}""".format(id))
    return make_response(jsonify(data), 200)

@app.route("/company", methods=["POST"])
def add_company():
    cur = mysql.connection.cursor()
    info = request.get_json()
    company_name = info["company_name"]
    head_office_address = info["head_office_address"]
    other_company_details = info["other_company_details"]
    cur.execute(
        """ INSERT INTO company (company_name, head_office_address, other_company_details) VALUE (%s, %s, %s)""",
        (company_name, head_office_address, other_company_details),
    )
    mysql.connection.commit()
    print("row(s) affected :{}".format(cur.rowcount))
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "New company added successfully", "rows_affected": rows_affected}
        ),
        201,
    )

@app.route("/company/<int:id>", methods=["PUT"])
def update_company(id):
    cur = mysql.connection.cursor()
    info = request.get_json()
    company_name = info["company_name"]
    head_office_address = info["head_office_address"]
    other_company_details = info["other_company_details"]
    cur.execute(
        """ INSERT INTO companies (company_name, head_office_address, other_company_details) VALUE (%s, %s, %s)""",
        (company_name, head_office_address, other_company_details),
    )
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "Company updated successfully", "rows_affected": rows_affected}
        ),
        200,
    )


@app.route("/company/<int:id>", methods=["DELETE"])
def delete_actor(id):
    cur = mysql.connection.cursor()
    cur.execute(""" DELETE FROM companies where company_id = %s """, (id,))
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "company deleted successfully", "rows_affected": rows_affected}
        ),
        200,
    )


if __name__ == "__main__":
    app.run(debug=True)
