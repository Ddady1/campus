

class Pixel:

    def __init__(self, x=0, y=0, red=0, green=0, blue=0):

        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue


    def set_coords(self, x, y):

        self._x = x
        self._y = y



    def set_greyscale(self):

        pixel_sum = sum(self._red, self._green, self._blue)
        self._red = pixel_sum
        self._green = pixel_sum
        self._blue = pixel_sum


    def print_pixel_info(self):

        colors = [self._red, self._green, self._blue]
        count = colors.count(0)
        color_str = ('X: ' + self._x + ', Y: ' + self._y + ', Color:' + '(' + self._red + ', ' + self._green + ', ' + self._blue + ')')
        if count >= 2:
            print(color_str + colors)

        print('X: ' + self._x + ', Y: ' + self._y + ', Color:' + '(' + self._red + ', ' + self._green + ', ' + self._blue + ')')

