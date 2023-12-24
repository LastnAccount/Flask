from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '37707'
app.config['MYSQL_DB'] = 'trytry'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def Index():
    if request.method == 'POST':
        search_query = request.form['search']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM students WHERE name LIKE %s OR email LIKE %s", ('%' + search_query + '%', '%' + search_query + '%'))
        data = cur.fetchall()
        cur.close()
        return render_template('index2.html', students=data)
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM trytry.companies")
    data = cur.fetchall()
    cur.close()

    return render_template('index2.html', students=data)



@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        company_name = request.form['company_name']
        head_office_address = request.form['head_office_address']
        other_company_details = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (name, email, phone) VALUES (%s, %s, %s)", (company_name, head_office_address, other_company_details))
        mysql.connection.commit()
        return redirect(url_for('Index'))
    
    

@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (company_id,))
    mysql.connection.commit()
    return redirect(url_for('Index'))



@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        company_id = request.form['company_id']
        company_name = request.form['company_name']
        head_office_address = request.form['head_office_address']
        other_company_details = request.form['other_company_details']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE students
               SET name=%s, email=%s, phone=%s
               WHERE id=%s
            """, (company_name, head_office_address, other_company_details, company_id))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))



if __name__ == "__main__":
    app.run(debug=True)
