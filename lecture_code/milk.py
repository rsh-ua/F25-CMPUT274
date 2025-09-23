
def milkPurchase(alPrice, oatPrice, soyPrice):
  '''
  milkPurchase returns a string specififying which
               milk to purchase based on the prices
               of those milks

  alPrice  - float, represents price of almond milk
             per 100ml
  oatPrice - float, represents price of oat milk
             per 100ml
  soyPrice - float, represents price of oat milk
             per 100ml
  returns  - a string from the set ("Soy", "Almond",
             "Oat", "Nothing)

  Examples:
    milkPurchase(0.39, 0.22, 0.25) -> "Almond"
    milkPurcase(0.29, 0.27, 0.19) -> "Soy"
  '''

  if alPrice < 0.2:
    return "Almond"
  elif oatPrice < 0.2:
    return "Oat"
  elif soyPrice < 0.2:
    return "Soy"
  elif alPrice < 0.45:
    return "Almond"
  elif oatPrice < 0.4:
    return "Oat"
  elif soyPrice < 0.37:
    return "Soy"
  else:
    return "Nothing"
