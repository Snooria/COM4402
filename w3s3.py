# Practice#
#1.
# for row in range(3):
#                  for col in range(4):
#                      print("*", end="")
#                  print()
#----------------------------#

#2.
# rows = 4
# for i in range(1, rows+1):
#     for j in range(i):
#         print("*", end="")
#     print()

#-----------------#

# Activity no.1 NUMBER TRIANGLE
# rows=5
# for i in range(1, rows+1):
#     for j in range(i):
#         print("*", end="")
#     print()

# Activity no 2.  MULTIPLICATION GRID

size=5

# for row in range(1, size+1):
#     line=""
#     for col in range(1, size+1):
#         line +=f"{row*col:3}"
#     print(line)

#Nested Loops and Real World Patterns Problems#

# 1. Right-Angled Triangle of Stars
# Print a right-angled triangle of stars with 5 rows.

# row=5
#
# for row in range(5):
#     for col in range(row):
#         print("*",end=" ")
#     print()

####---------------------------------####

#2. Number Triangle (Row Number)
#Print a triangle where each row i (1 to 5) contains the row number repeated i times.

# row=5
# need row from 1 to 5 so add row+1.
# for i in range(1, row+1):
    # we need triangle to repeat the row number in each row. so include i in print output.
    # for j in range(i):
    #     print(i,end=" ")
    # print()

######------------------------------------------------######

# 3. Increasing Number Triangle
# Print a triangle where numbers increase from 1 across the rows.

# n=3
# num=1
# for i in range(1, n+1):
#     for col in range(1, i+1):
#         print(num, end=' ')
#         num=num+1
#     print()

####-------------------####

#4. Square Multiplication Grid
#Print a 5×5 multiplication grid where each cell is row * column.


# size = 5
#
# for row in range(1, size + 1):
#     line = ""
#     for col in range(1, size + 1):
#         line += f"{row * col:3}"
#     print(line)


####------------------------------####

# 5. Coordinate Grid
# Print a 3×4 grid showing coordinates (row, col).
#
# rows = 3
# cols = 4
#
# for r in range(rows):
#     line = ""
#     for c in range(cols):
#         line += f"({r},{c}) "
#     print(line.strip())

####------------------------------####

# 6. Hollow Square of Stars
# Print a 5×5 hollow square: stars on the border, spaces inside.

# size = 5
#
# for r in range(size):
#     line = ""
#     for c in range(size):
#         if r == 0 or r == size - 1 or c == 0 or c == size - 1:
#             line += "*"
#         else:
#             line += " "
#     print(line)

####---------------------------####

# 7. Centered Pyramid of Stars
# Print a centered pyramid with 4 rows.

# rows = 4
#
# for i in range(1, rows + 1):
#     spaces = rows - i        # leading spaces
#     stars = 2 * i - 1        # odd number of stars
#     print(" " * spaces + "*" * stars)


# 8. Times Table Block (2–4 by 1–5)
# Print multiplication tables for 2, 3, and 4, each from ×1 to ×5, in a block.

# for mul in range(1, 6):
#     line = ""
#     for table in range(2, 5):
#         result = table * mul
#         line += f"{table} x {mul} = {result:<2}   "
#     print(line.rstrip())

####------------------------------------####

# 9. Checkerboard Pattern
# Print an 8×8 checkerboard using # and . alternately.

# size = 8
#
# for r in range(size):
#     line = ""
#     for c in range(size):
#         if (r + c) % 2 == 0:
#             line += "#"
#         else:
#             line += "."
#     print(line)

####-----------------------------------####

# 10. Pascal-like Triangle (Simple Sums)
# Start with 1 at the top.
# Each number (except edges) is the sum of the two numbers above it.
# Generate 5 rows.

