def is_armstrong_number(number):

    if type(number) != int or number < 0:
      raise Exception('Invalid input')

    return True if number == sum([(int(num)**len(str(number))) for num in str(number)]) else False