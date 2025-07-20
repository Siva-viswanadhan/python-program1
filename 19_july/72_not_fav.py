#Create a list of six school subjects.
# Ask the user which of these subjects they don't like. Delete the subject they have chosen from
# the list before you display the list again.


def notfav_subjects(subjects, user_input):
    if user_input in subjects:
        subjects.remove(user_input)
    return subjects

subjects = ['maths', 'biology', 'history', 'english', 'physics']
user_input = 'history'
print(notfav_subjects(subjects, user_input))