from flask import Flask, render_template, request, redirect
app = Flask(__name__)  # app object

# http://127.0.0.1:5000


data = [{"username": 'Thayammal', "password": '123456'},
        {"username": 'Sanju', 'password': 'cs2003'}]


@app.route('/login', methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        username = request.form.get("u_name")
        password = request.form.get("pwd")
        for entry in data:
            if entry["username"] == username:
                if entry["password"] == password:
                    return render_template('loggedin.html', username=username, password=password)
                else:
                    return "Incorrect Password"
            else:
                return f"<h1> Username {username} does not exist </h1> <a href='/register'> Go Back </a>"
               # return f"<h1> Welcome {username} </h1>"
    return render_template('index.html')


@app.route('/register', methods=["GET", "POST"])
def register_page():
    if request.method == "POST":
        username = request.form.get("u_name")
        password = request.form.get("pwd")
        new_user = {}
        new_user["username"] = username
        new_user["password"] = password
        data.append(new_user)
        return redirect('/login')
    return render_template('register.html')


app.run(debug=True)
