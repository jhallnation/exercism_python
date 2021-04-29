class PhoneNumber:
    def __init__(self, number):
     
      numList = [int(num) for num in list(number) if num.isdigit()]

      if len(numList) == 11 and numList[0] == 1:
        numList.pop(0)

      if len(numList) != 10 or numList[0] < 2 or numList[3] < 2:
        raise ValueError("Invalid number")

      self.number = ''.join([str(num) for num in numList])
      self.area_code = self.number[:3]


    def pretty(self):
      return '({})-{}-{}'.format(self.number[:3], self.number[3:6], self.number[6:])