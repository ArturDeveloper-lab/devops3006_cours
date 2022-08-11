# class Rectangle:
#     def __init__(self, width, height, color):
#         self.width = width
#         self.height = height
#         self.color = color
#
#     def area(self):
#         return self.width * self.height
#
#     # Create some instances of the class
#
#
# default_rectangle = Rectangle(2, 3,4)
# print(default_rectangle.color)  # blue
#
# red_rectangle = Rectangle(2, 3, 'red')
# print(red_rectangle.color)  # red



class User:
    def __init__(self,user_id, username):
        self.user_id = user_id
        self.username = username

user = User(6666,222)

print(user.user_id)
print(user.username)