import numpy as np

def calculate(input_list):
  if len(input_list) < 9:
    raise ValueError("List must contain nine numbers.")
    
  a = np.array(input_list)
  matrix = a.reshape(3,3)

  mean = [list(matrix.mean(axis=0)), list(matrix.mean(axis=1)), matrix.mean()]
  variance = [list(matrix.var(axis=0)), list(matrix.var(axis=1)), matrix.var()]
  std_dev = [list(matrix.std(axis=0)), list(matrix.std(axis=1)), matrix.std()]
  max_val = [list(matrix.max(axis=0)), list(matrix.max(axis=1)), matrix.max()]
  min_val = [list(matrix.min(axis=0)), list(matrix.min(axis=1)), matrix.min()]
  sum_val = [list(matrix.sum(axis=0)), list(matrix.sum(axis=1)), matrix.sum()]

  
  calculations = {
    'mean': mean,
    'variance': variance,
    'standard deviation': std_dev,
    'max': max_val,
    'min': min_val,
    'sum': sum_val
  }



  return calculations
