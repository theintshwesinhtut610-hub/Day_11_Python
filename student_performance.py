grades = ("A", "B", "C", "D", "F")

students = [
    {"name": "Mg Mg", "age": 20, "hours": 3, "score": 85},
    {"name": "Aye Aye", "age": 19, "hours": 2, "score": 75},
    {"name": "Ko Ko", "age": 21, "hours": 4, "score": 65},
    {"name": "Su Su", "age": 20, "hours": 3, "score": 55},
    {"name": "Hla Hla", "age": 19, "hours": 5, "score": 35}
]

def calculate_average(scores):
    return sum(scores) / len(scores)

def classify_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"

def count_passed(students):
    return sum(1 for s in students if s["score"] >= 40)

scores = [s["score"] for s in students]

print("===== STUDENT PERFORMANCE REPORT =====")

for s in students:
    print(s["name"], s["age"], s["hours"],
          s["score"], classify_grade(s["score"]))

print("Average Score:", calculate_average(scores))
print("Passed Students:", count_passed(students))
print("Failed Students:", len(students) - count_passed(students))
print("Grade Categories:", grades)