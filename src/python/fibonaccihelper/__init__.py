import numpy


class FibonacciHelper(object):
    def get_fibonacci_number(self, number):
        # Doing this numpy stuff just to show how a 3rd party library would be used with pants build system
        if number < 0:
            number = numpy.absolute(number)

        if number == 0:
            return 0
        elif number == 1:
            return 1

        return self.get_fibonacci_number(number - 1) + self.get_fibonacci_number(number - 2)
