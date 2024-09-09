class Rectangle:
    def __init__(self, length: float, width: float, color: str):
        self.length = length
        self.width = width
        self.color = color

    def show_attributes(self):
        return f'length = {self.length}, width = {self.width}, color = {self.color}'

    def area(self):
        return self.length * self.width


def highest_area_rectangle(rectangles):
    for i in range(len(rectangles)):
        highest_area = 0
        if rectangles[i].area() > highest_area:
            highest_area = rectangles[i].area()
            highest_area_rectangle_pos = i
            return highest_area, highest_area_rectangle_pos

def smallest_width_rectangle(rectangles):
    for i in range(len(rectangles)):
        smallest_width = rectangles[i].width
        if rectangles[i].width < smallest_width:
            smallest_width = rectangles[i].area()
            smallest_width_rectangle_pos = i
            return smallest_width, smallest_width_rectangle_pos




if __name__ == '__main__':
    rectangles = []
    for i in range(5):
        length = float(input('What is the length?'))
        width = float(input('What is the width?'))
        color = input('What is the color?').lower()
        rectangles.append(Rectangle(length, width, color))

    biggest_area_rectangle_position = highest_area_rectangle(rectangles)[1]
    smallest_width_rectangle_position = smallest_width_rectangle(rectangles)[1]


"""
• Locate all Rectangles with the colour “red” (case-insensitive), store them in a new list and display them once
all Rectangles have been processed. If there are no red Rectangles, display a message indicating this to the
user.
• Ask the user to enter a colour, then repeat the above action to find, store and display all Rectangles of that
colour.
Note: You should consider how you might use functions to improve your code"""