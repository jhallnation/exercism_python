def convert(number):
  response = ''

  if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
    return str(number)

  if number % 3 == 0:
    response += 'Pling'

  if number % 5 == 0:
    response += 'Plang'

  if number % 7 == 0:
    response += 'Plong'

  return response
