
month_convert = {
    # key = value
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "Nivember",
    "Dec": "December",
}

print (month_convert["Jan"])

# print (month_convert["Sam"])        #  None
# print (month_convert["Sam", "Not a valid key"])   #  Not a valid key

print (month_convert.get("Feb"))


original_marks = {'Physics':76, 'Maths':87}

marks = original_marks.copy()

print('Original Marks:', original_marks)
print('Copied Marks:', marks)

print(marks.get('Physics'))

print(marks.keys)

internal_marks = {'Chemistry':87}
marks.update(internal_marks)

element = marks.pop('Chemistry')
print('Popped Marks:', element)
