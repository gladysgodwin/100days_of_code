student_height = input("Input a list of student height\n").split()

for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])

total = 0
count = 0
for num in student_height:
    total += num
    count += 1
average = total/count

print(round(average))
