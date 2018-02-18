import pandas as pd

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liaison'},
                         {'Name': 'James', 'Role': 'Grader'}])

#staff_df['Date'] = pd.Series({1: 'January'})
staff_df = staff_df.set_index('Name')

student_df = pd.DataFrame([{'Name': 'James', 'Role': 'Business'},
                         {'Name': 'Mike', 'Role': 'Law'},
                         {'Name': 'Sally', 'Role': 'Engineering'}])

student_df = student_df.set_index('Name')

# how= 'inner | outer | left | right'
print pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True)