# In your boat.py file, write your boat object using your notes from the Intro to Programming class.
# Define your attributes for your constructor.
# Utilize the property() along with the getter and setter for each of your variable attributes.
# Be sure to test your class and properties.
class Boat:
    def __init__(self, size, color, material):
        self._size = size
        self._color = color
        self._material = material

    def motor_on_off(self):
        print('The motor is on')

    @property
    def size(self):
        return self.size

    @size.getter
    def get_size(self):
        return self._size

    @size.setter
    def size(self, num):
        self._size = num

    @property
    def color(self):
        return self.color

    @color.getter
    def get_color(self):
        return self._color

    @color.setter
    def color(self, type):
        self._color = type

    @property
    def material(self):
        return self.material

    @material.getter
    def get_material(self):
        return self._material

    @material.setter
    def material(self, mat):
        self._material = mat


my_boat = Boat('yacht', 'white', 'metal')
print(my_boat._size)
print(my_boat.motor_on_off())
