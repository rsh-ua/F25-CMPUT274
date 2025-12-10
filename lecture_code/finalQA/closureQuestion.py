
def g(n):
  captureMe = n*2
  def f(n):
    return 7*(n+captureMe)
  return f


def pairOfClosures(n):
  captured = [n,n*2,n*3]
  def f1(x):
    captured[x] = captured[x]*2
    return captured
  def f2(y):
    return captured[y]
  return (f1, f2)


def makeCar(colour, kms):
  carList = [colour, kms]
  def car(op, arg):
    if op == "paint":
      # arg is the color
      carList[0] = arg
    if op == "drive":
      # arg is number of kms driven
      carList[1] = carList[1] + arg
    if op == "read":
      if arg == "colour":
        return carList[0]
      if arg == "odometer":
        return carList[1]
  return car
