# Calculating the average height from an array of heights
# IMPORTANT! We should not use sum() & len() for this exercise. only loops.
# Example Input: 156 178 165 171 187
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

average_height = 0
sum_of_heights = 0
len_of_heights = 0

for height in student_heights:
    sum_of_heights += height
    len_of_heights += 1

average_height = round(sum_of_heights / len_of_heights)

print(average_height)
