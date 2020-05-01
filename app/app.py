from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask.cli import FlaskGroup
from datetime import datetime
import os

def configuring_database(app=None):
    engine = 'postgres://%s:%s@%s:%s/%s' % (
        os.environ['POSTGRES_USER'], 
        os.environ['POSTGRES_PASSWORD'], 
        'db', '5432',
        os.environ['POSTGRES_DB']
    )

    app.config['SQLALCHEMY_DATABASE_URI'] = engine
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return SQLAlchemy(app)

# Initializing app and configuring it
app = Flask(__name__)
cli = FlaskGroup(app)
db = configuring_database(app)

# Defining the project model
class Todo(db.Model):
    __tablename__ = "todo"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_completed = db.Column(db.String(50))

    def __repr__(self):
        return '<Task %r>' % self.id

# Main route of the project
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        task_completed = request.form['completed']

        new_task = Todo(content=task_content, date_completed=task_completed)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue adding your task"
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:id>")
def delete(id):
    delete_task = Todo.query.get_or_404(id)

    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting it"

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == "POST":
        task.content = request.form['content']
        task.date_completed = request.form['completed']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return "Issue updating the Task"
    else:
        return render_template('update.html', task=task)


# Migrating Database
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    print('Created database!')

# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0')