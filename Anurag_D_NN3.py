import sys; args = sys.argv[1:]
import math, random

# t_funct is symbol of transfer functions: 'T1', 'T2', 'T3', or 'T4'
# input is a list of input (summation) values of the current layer
# returns a list of output values of the current layer
def transfer(t_funct, input):
   if t_funct == 'T3': return [1 / (1 + math.e**-x) for x in input]
   elif t_funct == 'T4': return [-1+2/(1+math.e**-x) for x in input]
   elif t_funct == 'T2': return [x if x > 0 else 0 for x in input]
   else: return [x for x in input]

# returns a list of dot_product result. the len of the list == stage
# dot_product([x1, x2, x3], [w11, w21, w31, w12, w22, w32], 2) => [x1*w11 + x2*w21 + x3*w31, x1*w12, x2*w22, x3*w32] 
def dot_product(input, weights, stage):
   return [sum([input[x]*weights[x+s*len(input)] for x in range(len(input))]) for s in range(stage)]

# Complete the whole forward feeding for one input(training) set
# return updated x_vals and error of the one forward feeding
def ff(ts, xv, weights, t_funct):

   ''' ff coding goes here '''
   x_vals = xv
   for a, v in list(enumerate(weights))[1:]:
      x_vals[a] = transfer(t_funct, dot_product(x_vals[a-1], weights[a-1], len(xv[a])))
   x_vals[-1] = [x_vals[-2][a] * weights[-1][a] for a in range(len(x_vals[-1]))]
   xv = x_vals
   err = sum([(ts[-1 * len(xv[-1]) + i] - xv[-1][i])**2 for i in range(len(xv[-1]))]) / 2
   return xv, err

# Complete the back propagation with one training set and corresponding x_vals and weights
# update E_vals (ev) and negative_grad, and then return those two lists
def bp(ts, xv, weights):  


   ''' bp coding goes here '''
   negative_grad, xv, weights, ev = [[] for a in range(len(weights))], xv[::-1], weights[::-1], [[*i] for i in xv][::-1]
   for a in range(len(xv)-1):
      if a == 0: 
         ev[a][0] = ts[-1] - xv[a][0]
         continue
      for b in range(len(xv[a])):
         ev[a][b] = xv[a][b] * (1 - xv[a][b]) * sum(weights[a-1][b+len(xv[a]) * c] * ev[a-1][c] for c in range(len(xv[a-1])))
   weights, negative_grad, xv, ev = weights[::-1], negative_grad[::-1], xv[::-1], ev[::-1]
   for a in range(len(weights)):
      for b in range(len(weights[a])):
         negative_grad[a].append(xv[a][b%len(xv[a])] * ev[a+1][b//len(xv[a])])
   return ev, negative_grad

# update all weights and return the new weights
# Challenge: one line solution is possible
def update_weights(weights, negative_grad, alpha):

   ''' update weights (modify NN) code goes here '''
   return [[weights[a][b] + negative_grad[a][b] * alpha for b in range(len(weights[a]))] for a in range(len(weights))]

def evaluate(x, y, operator, value):
    if operator == "<=": return 1 if x**2 + y**2 <= value else 0
    elif operator == ">=": return 1 if x**2 + y**2 >= value else 0
    elif operator == "<": return 1 if x**2 + y**2 < value else 0
    else: return 1 if x**2 + y**2 > value else 0

def main():
   t_funct = 'T3' # we default the transfer(activation) function as 1 / (1 + math.e**(-x))
   ''' work on training_set and layer_count '''
   equation, operator, value = args[0], "", 0
   if(equation.find("<=") != -1): 
       operator = "<="
       value = float(equation[equation.index("<=")+2:])
   elif(equation.find(">=") != -1): 
       operator = ">="
       value = float(equation[equation.index(">=")+2:])
   elif(equation.find("<") != -1): 
       operator = "<"
       value = float(equation[equation.index("<")+1:])
   else: 
       operator = ">"
       value = float(equation[equation.index(">")+1:])
   print(value, operator)

   size, training_set = 10000, []
   for a in range(size):
       x, y =random.uniform(-1.5, 1.5), random.uniform(-1.5, 1.5)
       evaluation = evaluate(x, y, operator, value)
       training_set.append([x, y, evaluation])

   # list of lists
   #print (training_set) #[[1.0, -1.0, 1.0], [-1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [-1.0, -1.0, 1.0], [0.0, 0.0, 0.0]]

   layer_counts = [3, 30, 10, 1, 1] # set the number of layers
   print ('layer counts', layer_counts) # This is the first output. [3, 2, 1, 1] with teh given x_gate.txt

   ''' build NN: x nodes and weights '''
   x_vals = [[temp[0:len(temp)-1]] for temp in training_set] # x_vals starts with first input values
   #print (x_vals) # [[[1.0, -1.0]], [[-1.0, 1.0]], [[1.0, 1.0]], [[-1.0, -1.0]], [[0.0, 0.0]]]
   # make the x value structure of the NN by putting bias and initial value 0s.
   for i in range(len(training_set)):
      x_vals[i] = [training_set[i][:-1] + [1.0] if j == 0 else [0 for k in range(layer_counts[j])] for j in range(len(layer_counts))]
   #print ('x_vals', x_vals, myLines) # [[[1.0, -1.0, 1.0], [0, 0], [0], [0]], [[-1.0, 1.0, 1.0], [0, 0], [0], [0]], ...

   # by using the layer counts, set initial weights [3, 2, 1, 1] => 3*2 + 2*1 + 1*1: Total 6, 2, and 1 weights are needed
   weights = []
   for i in range(len(layer_counts) - 1):
      if i != len(layer_counts) - 2:
         weights.append([round(random.uniform(-2.0, 2.0), 2) for j in range(layer_counts[i]*layer_counts[i+1])])
      else:
         weights.append([round(random.uniform(-2.0, 2.0), 2) for j in range(layer_counts[-1])])
   #weights = [[1.35, -1.34, -1.66, -0.55], [-1.08, -0.7], [-0.6]] 
   #print(weights)
   #weights = [[1.35, -1.34, -1.66, -0.55, -0.9, -0.58, -1.0, 1.78], [-1.08, -0.7], [-0.6]]   #Example 2
   #print ('weights', weights)    #[[2.0274715389784507e-05, -3.9375970265443985, 2.4827119599531016, 0.00014994269071843774, -3.6634876683142332, -1.9655046461270405]
                        #[-3.7349985848630634, 3.5846029322774617]
                        #[2.98900741942973]]

   # build the structure of BP NN: E nodes and negative_gradients 
   E_vals = [[[*i] for i in j] for j in x_vals]  #copy elements from x_vals, E_vals has the same structures with x_vals
   negative_grad = [[0 for i in j] for j in weights]  #copy elements from weights, negative gradients has the same structures with weights
   errors = [10 for a in range(len(training_set))]  # Whenever FF is done once, error will be updated. Start with 10 (a big num)
   count = 1  # count how many times you trained the network, this can be used for index calc or for decision making of 'restart'
   alpha = 0.3
   # calculate the initail error sum. After each forward feeding (# of training sets), calculate the error and store at error list
   count = 0
   while sum(errors)/len(errors) > 0.005:
    #print(sum(errors)/len(errors))
    #prev_sum = sum(errors)  
   #print(sum(errors)/len(errors)) 
    for k in range(len(training_set)):
       x_vals[k], errors[k] = ff(training_set[k], x_vals[k], weights, t_funct)
      # print(errors, sum(errors))
       ev, negative_gradient = bp(training_set[k], x_vals[k], weights)
       weights = update_weights(weights, negative_gradient, alpha)
    count += 1
   #  if(count == 100000): 
   #     weights = [[round(random.uniform(-2.0, 2.0), 2) for j in range(layer_counts[i]*layer_counts[i+1])]  for i in range(len(layer_counts)-1)]
   #     count = 0
    print (str(''.join([str(w)[1:-1] + '\n' for w in weights]))[:-2])

   ''' 
   while err is too big, reset all weights as random values and re-calculate the error sum.
   
   '''

   ''' 
   while err does not reach to the goal and count is not too big,
      update x_vals and errors by calling ff()
      whenever all training sets are forward fed, 
         check error sum and change alpha or reset weights if it's needed
      update E_vals and negative_grad by calling bp()
      update weights
      count++
   '''
   # print final weights of the working NN
   #print ('h:')
   for k in range(len(training_set)):
      x_vals[k], errors[k] = ff(training_set[k], x_vals[k], weights, t_funct)
   # print(errors)
   # print(x_vals)
   print([x_vals[a][-1] for a in range(len(x_vals))], errors)# + str(training_set))
  # print (sum(errors))
if __name__ == '__main__': main()
# Dhruv Anurag 5 2024