# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
height_total = 0
for height in student_heights:
  height_total+=height

number_of_heights = 0
for number in student_heights:
  number_of_heights+=1
  
#print(round(height_total))
#print(number_of_heights)

answer = round(height_total / number_of_heights)
print(answer)
#Average height rounded to the nearest whole number = 164
#Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

#Example Input: 156 178 165 171 187
#Example Output: 171



