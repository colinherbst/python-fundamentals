# In your guitar.py file, write your boat object using your notes from the Intro to Programming class.
# Define your attributes for your constructor.
# Utilize the property() along with the getter and setter for each of your variable attributes.
# Be sure to test your class and properties.
class Guitar:
    def __init__(self, shape, color, material):
        self._shape = shape
        self._color = color
        self._material = material

    def amp_on_off(self):
        print('The amp is on')

    @property
    def shape(self):
        return self.shape

    @shape.getter
    def get_shape(self):
        return self._shape

    @shape.setter
    def shape(self, num):
        self._shape = num

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


my_guitar = Guitar('electric', 'blue', 'plastic')
print(my_guitar._shape)
print(my_guitar.amp_on_off())
