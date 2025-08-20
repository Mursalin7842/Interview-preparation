test={"name":["adib","ali","ahmed","sara","sara"],
      "age":[20,21,22,23,24],"cgpa":[3.2,3.4,3.6,3.8,4.0]}

for name,age,cgpa in zip(test["name"],test["age"],test["cgpa"]):
    print(f"{name} is {age} years old. CGPA = {cgpa}")
print()