student = {
    "name" : "aditee",
    "Age" : 15,
    "Marks in English" : 89,
    "Marks in Hindi" : 86,
    "Marks in Physics" : 91,
    "Marks in Chemistry" : 91,
    "marks in Physical Education" : 96,

}
def calculate_results(student):
    total = 0
    for key,value in student.items():
        if "marks" in key.lower():
            total = total + value
        percentage = round((total/500)*100,2)
    return total,percentage
# print(calculate_results(student))

def get_grade(percentage):
    if percentage >= 90:
        return "A"
    elif  80 <= percentage < 90:
        return "B"
    elif  70 <= percentage < 80:
        return "C"
    elif  percentage < 70:
        return "Go Home"
    
total, percentage = calculate_results(student)
grade = get_grade(percentage)
print("="*25)
print(f"REPORT CARD - {student['name'].title()}")
print("="*25)
# print(f"Total: {total}","/500")
# print(f"Percentage: {percentage}%")
# print(f"Grade: {grade}")
print(f"{'Total' :<20}: {total}","/500")
print(f"{'Percentage' :<20}: {percentage:.2f}%")
print(f"{'Grade':<20}: {grade}")
print("="*25)
