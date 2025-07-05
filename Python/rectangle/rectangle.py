import calculate

# Prompt user for rectangle dimensions and find area and perimeter
width = float(input("Rectangle Width: ").strip())
length = float(input("Rectangle length: ").strip())

print(f"The area of a rectangle of length {length} and width {width} is {calculate.rectangle_area(length, width)}")
print(f"The perimeter of a rectangle of length {length} and width {width} is {calculate.rectangle_perimeter(length, width)}")