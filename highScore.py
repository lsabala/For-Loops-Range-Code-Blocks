# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
largest_score = student_scores[0]

for number in student_scores:
  if number > largest_score:
    largest_score = number 

print(f"The highest score in the class is: {largest_score}")


#Important you are not allowed to use the max or min functions. The output words must match the example. i.e
#The highest score in the class is: x



