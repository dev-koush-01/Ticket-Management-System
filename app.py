from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Timezone setup
timezone = pytz.timezone("Asia/Kolkata")  # Set to your correct timezone

class ToDo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    ticketNo = db.Column(db.String, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="Not Entered")
    entry_time = db.Column(db.DateTime, nullable=True)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.ticketNo}"

@app.route("/", methods=['GET', 'POST'])
def myTodo():
    if request.method == "POST":
        ticketNo = request.form['title']
        todo = ToDo(ticketNo=ticketNo)
        db.session.add(todo)
        db.session.commit()
        return redirect("/")

    # Handle search and filter
    search = request.args.get('search', '')
    status_filter = request.args.get('status', '')

    query = ToDo.query
    if search:
        query = query.filter(ToDo.ticketNo.contains(search))
    if status_filter == "entered":
        query = query.filter(ToDo.status == "Entered")
    elif status_filter == "not_entered":
        query = query.filter(ToDo.status == "Not Entered")

    allTodo = query.all()
    message = "No records found." if not allTodo else None

    return render_template(
        "index.html", 
        allTodo=allTodo, 
        message=message, 
        search=search, 
        status=status_filter
    )

@app.route("/delete/<int:sno>")
def delete(sno):
    search = request.args.get('search', '')
    status = request.args.get('status', '')

    todo = ToDo.query.filter_by(sno=sno).first()
    if todo:
        db.session.delete(todo)
        db.session.commit()

    return redirect(url_for("myTodo", search=search, status=status))

@app.route("/enter/<int:sno>")
def enter(sno):
    search = request.args.get('search', '')
    status = request.args.get('status', '')

    todo = ToDo.query.filter_by(sno=sno).first()
    if todo:
        todo.status = "Entered"
        todo.entry_time = datetime.now(timezone)
        db.session.commit()

    return redirect(url_for("myTodo", search=search, status=status))

@app.route("/reset")
def reset():
    todos = ToDo.query.all()
    for todo in todos:
        todo.status = "Not Entered"
        todo.entry_time = None
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=3000)
