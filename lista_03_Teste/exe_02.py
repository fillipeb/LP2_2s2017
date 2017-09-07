def same_first_last(nums):
  retorno = True
  if nums==[] or nums[0]!= nums[-1]:
    retorno = False  
  return retorno