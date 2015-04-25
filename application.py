from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index_page():

    return render_template("index.html")

@app.route("/application-form")
def application_form():

    return render_template("application-form.html")

@app.route("/application", methods=['GET', 'POST'])
def application_return():
	firstname = request.form.get("firstname")
	lastname = request.form.get("lastname")
	position = request.form.get("position")
	salary = request.form.get("salary")

	return render_template("application-confirm.html", firstname=firstname, lastname=lastname, position=position, salary=salary)


if __name__ == "__main__":
    app.run(debug=True)