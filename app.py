from flask import Flask,render_template

app=Flask(__name__)

lst_jobs = [
    {
        'id' : 1,
        'title' : "Data Analyst",
        'location' : "Bengaluru, India",
        'salary' : "Rs. 15,00,000"
    },
    {
        'id' : 2,
        'title' : "Data Scientist",
        'location' : "Delhi, India",
        'salary' : "Rs. 20,00,000"
    },
    {
        'id' : 3,
        'title' : "Frontend Engineer",
        'location' : "Remote"
    },
    {
        'id' : 4,
        'title' : "Backend Engineer",
        'location' : "San Francisco, USA",
        'salary' : "US$, 120.000"
    }
]

@app.route("/")
def hello_world():
    return render_template("home.html", jobs=lst_jobs, company_name='Jovian INC')


if __name__ == "__main__":
  # remember to change debug to False in production
  app.run(host='0.0.0.0',debug=True) 