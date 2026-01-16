from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///grades.db'
db = SQLAlchemy(app)

# Course evaluation weights (updated as per new formula)
EVALUATION_WEIGHTS = {
    'Lab 1': 0.05,  # 6 labs, each 5% (total 30%)
    'Lab 2': 0.05,
    'Lab 3': 0.05,
    'Lab 4': 0.05,
    'Lab 5': 0.05,
    'Lab 6': 0.05,
    'Midterm': 0.20,
    'Final': 0.30,
    'Project': 0.20
}

class GradeItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Float, nullable=False)

def calculate_final_grade(items):
    total = 0.0
    for item in items:
        weight = EVALUATION_WEIGHTS.get(item.test, 0)
        total += item.score * weight
    return total

@app.route('/')
def index():
    items = GradeItem.query.all()
    final_grade = calculate_final_grade(items)
    return render_template('index.html', items=items, final_grade=final_grade)

@app.route('/add', methods=['POST'])
def add():
    test = request.form['test']
    score = float(request.form['score'])
    new_item = GradeItem(test=test, score=score)
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>')
def delete(item_id):
    item = GradeItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit(item_id):
    item = GradeItem.query.get_or_404(item_id)
    if request.method == 'POST':
        item.test = request.form['test']
        item.score = float(request.form['score'])
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', item=item)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
