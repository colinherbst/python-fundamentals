# In your horse.py file, write your boat object using your notes from the Intro to Programming class.
# Define your attributes for your constructor.
# Utilize the property() along with the getter and setter for each of your variable attributes.
# Be sure to test your class and properties.
class Horse:
    def __init__(self, weight, hair_color, hair_length):
        self._weight = weight
        self._hair_color = hair_color
        self._hair_length = hair_length

    def horse_awake_asleep(self):
        print('The horse is awake')

    @property
    def weight(self):
        return self.weight

    @weight.getter
    def get_weight(self):
        return self._weight

    @weight.setter
    def weight(self, num):
        self._weight = num

    @property
    def hair_color(self):
        return self.hair_color

    @hair_color.getter
    def get_hair_color(self):
        return self._hair_color

    @hair_color.setter
    def hair_color(self, type):
        self._hair_color = type

    @property
    def hair_length(self):
        return self.hair_length

    @hair_length.getter
    def get_hair_length(self):
        return self._hair_length

    @hair_length.setter
    def hair_length(self, long):
        self._hair_length = long


my_horse = Horse(500, 'white', '3cm')
print(my_horse._weight)
print(my_horse.horse_awake_asleep())
