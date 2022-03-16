# In your watch.py file, write your boat object using your notes from the Intro to Programming class.
# Define your attributes for your constructor.
# Utilize the property() along with the getter and setter for each of your variable attributes.
# Be sure to test your class and properties.
class Watch:
    def __init__(self, face_size, color, material):
        self._face_size = face_size
        self._color = color
        self._material = material

    def time_military_standard(self):
        print('The time is standard')

    @property
    def face_size(self):
        return self.face_size

    @face_size.getter
    def get_face_size(self):
        return self._face_size

    @face_size.setter
    def face_size(self, num):
        self._face_size = num

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


my_watch = Watch('42mm', 'black', 'aluminium')
print(my_watch._face_size)
print(my_watch.time_military_standard())
