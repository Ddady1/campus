

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

        colors = (self._red, self._green, self._blue)
        pixel_sum = int(sum(colors) / len(colors))
        self._red = pixel_sum
        self._green = pixel_sum
        self._blue = pixel_sum


    def print_pixel_info(self):

        colors = (self._red, self._green, self._blue)
        for n in colors:
            if n != 0:
                pos = colors.index(n)
        if pos == 0:
            col = 'Red'
        elif pos == 1:
            col = 'Green'
        else:
            col = 'Blue'

        count = colors.count(0)
        color_str = 'X: ' + str(self._x) + ', Y: ' + str(self._y) + ', Color:'
        if count == 2:
            print(color_str, colors, col)
        else:
            print(color_str, colors)



def main():

    p = Pixel(5, 6, 250)
    p.print_pixel_info()
    p.set_greyscale()
    p.print_pixel_info()





if __name__ == '__main__':
    main()
