import csv
import pandas as pd

X = pd.read_csv('website\static\practiceq.csv', header=None)


@views.route('/practice/<num>', methods=['GET', 'POST'])
def practice(num):
    if request.method == 'POST':
        answer = request.form.get('answer')
        if answer == str(X[2][num]):
            print("Correct")
            flash("That's correct!", category="success")

        else:
            print("Incorrect")
            flash("That's not quite right", category="error")
        
        
    return render_template("quiz.html", question=X[0][num], figure=X[1][num], solution=X[2][num], num=num)