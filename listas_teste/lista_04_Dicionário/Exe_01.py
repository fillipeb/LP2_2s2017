def mdc(primeiro, segundo):
    if(primeiro==0):
      return segundo
    if (segundo==0):
      return primeiro
    if(primeiro != 0 and segundo != 0 ):
        if(primeiro > segundo):
            dividendo = primeiro
            divisor = segundo
        else:
            dividendo = segundo
            divisor = primeiro
        while( dividendo % divisor != 0 ):
            resto = dividendo % divisor
            dividendo = divisor
            divisor = resto
        return divisor
    else:
        print ("Os dois não podem ser zero")
def test_ex01():
  print ('mdc')
  assert mdc(15, 5) == 5