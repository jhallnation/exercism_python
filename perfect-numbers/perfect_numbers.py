def classify(number):

    if type(number) != int or number <= 0 or number % 1 != 0:
      raise ValueError(f'{number} is not a natural number!')

    aliquot = sum([num for num in range(1, number) if number % num == 0 ])

    if aliquot == number:
      return 'perfect'
    elif aliquot >= number:
      return 'abundant'
    else:
      return 'deficient'