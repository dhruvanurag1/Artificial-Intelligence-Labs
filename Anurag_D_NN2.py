import sys; args = sys.argv[1:]
myLines = open(args[0], "r").read().splitlines() 
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
   negative_grad, ev = [[] for a in range(len(weights))], [[*i] for i in xv]
   print(xv)
   if len(xv[-1]) == 1:
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
   else:
      negative_grad = [[0 for b in range(len(weights[a]))] for a in range(len(weights))]
      ev[-1][0] = ts[-2] - xv[-1][0]
      ev[-1][1] = ts[-1] - xv[-1][1]
      ev[-2][0] = xv[-2][0] * (1 - xv[-2][0]) * weights[-1][0] * ev[-1][0]
      ev[-2][1] = xv[-2][1] * (1 - xv[-2][1]) * weights[-1][1] * ev[-1][1]
      ev[-3][0] = xv[-3][0] * (1 - xv[-3][0]) * (weights[-2][0] * ev[-2][0] + weights[-2][3] * ev[-2][1])
      ev[-3][1] = xv[-3][1] * (1 - xv[-3][1]) * (weights[-2][1] * ev[-2][0] + weights[-2][4] * ev[-2][1])
      ev[-3][2] = xv[-3][2] * (1 - xv[-3][2]) * (weights[-2][2] * ev[-2][0] + weights[-2][5] * ev[-2][1])
      negative_grad[-1][0] = ev[-1][0] * xv[-2][0]
      negative_grad[-1][1] = ev[-1][1] * xv[-2][1]
      negative_grad[-2][0] = ev[-2][0] * xv[-3][0]
      negative_grad[-2][1] = ev[-2][0] * xv[-3][1]
      negative_grad[-2][2] = ev[-2][0] * xv[-3][2]
      negative_grad[-2][3] = ev[-2][1] * xv[-3][0]
      negative_grad[-2][4] = ev[-2][1] * xv[-3][1]
      negative_grad[-2][5] = ev[-2][1] * xv[-3][2]
      negative_grad[-3][0] = ev[-3][0] * xv[-4][0]
      negative_grad[-3][1] = ev[-3][0] * xv[-4][1]
      negative_grad[-3][2] = ev[-3][0] * xv[-4][2]
      negative_grad[-3][3] = ev[-3][0] * xv[-4][3]
      negative_grad[-3][4] = ev[-3][1] * xv[-4][0]
      negative_grad[-3][5] = ev[-3][1] * xv[-4][1]
      negative_grad[-3][6] = ev[-3][1] * xv[-4][2]
      negative_grad[-3][7] = ev[-3][1] * xv[-4][3]
      negative_grad[-3][8] = ev[-3][2] * xv[-4][0]
      negative_grad[-3][9] = ev[-3][2] * xv[-4][1]
      negative_grad[-3][10] = ev[-3][2] * xv[-4][2]
      negative_grad[-3][11] = ev[-3][2] * xv[-4][3]

   return ev, negative_grad 
# update all weights and return the new weights
# Challenge: one line solution is possible
def update_weights(weights, negative_grad, alpha):

   ''' update weights (modify NN) code goes here '''
   return [[weights[a][b] + negative_grad[a][b] * alpha for b in range(len(weights[a]))] for a in range(len(weights))]

def main():
   outputs = [[int(b) for b in a[a.index('=>')+2: len(a)].strip().split()] for a in myLines]
   t_funct = 'T3' # we default the transfer(activation) function as 1 / (1 + math.e**(-x))
   ''' work on training_set and layer_count '''
   training_set = [[int(b) for b in a[0:a.index('=>')].strip().split()] + [int(b) for b in a[a.index('=>')+2: len(a)].strip().split()] for a in myLines] 
   # list of lists
   #print (training_set) #[[1.0, -1.0, 1.0], [-1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [-1.0, -1.0, 1.0], [0.0, 0.0, 0.0]]

   layer_counts = [len(training_set[0]), len(outputs[0]) + 1, len(outputs[0]), len(outputs[0])]
   if len(outputs[0]) == 2: 
      layer_counts = [4, 3, 2, 2] # set the number of layers
   print ('layer counts', layer_counts) # This is the first output. [3, 2, 1, 1] with teh given x_gate.txt

   ''' build NN: x nodes and weights '''
   x_vals = [[temp[0:len(temp)-1]] for temp in training_set] # x_vals starts with first input values
   #print (x_vals) # [[[1.0, -1.0]], [[-1.0, 1.0]], [[1.0, 1.0]], [[-1.0, -1.0]], [[0.0, 0.0]]]
   # make the x value structure of the NN by putting bias and initial value 0s.
   for i in range(len(training_set)):
      x_vals[i] = [training_set[i][:-1] + [1.0] if j == 0 else [0 for k in range(layer_counts[j])] for j in range(len(layer_counts))]
   if len(outputs[0]) == 2: x_vals = [[[a for a in training_set[i][:-2]] + [1.0], [0 for i in range(3)], [0 for i in range(2)], [0 for i in range(2)]] for i in range(len(training_set))]
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
   error = [10 for a in range(len(training_set))]  # Whenever FF is done once, error will be updated. Start with 10 (a big num)
   count = 1  # count how many times you trained the network, this can be used for index calc or for decision making of 'restart'
   alpha = 0.3
   # calculate the initail error sum. After each forward feeding (# of training sets), calculate the error and store at error list
   count = 0
   errors = []
   while sum(errors) > 0.01:
    #prev_sum = sum(errors)   
    print('hi', x_vals)
    for k in range(len(training_set)):
       x_vals[k], errors[k] = ff(training_set[k], x_vals[k], weights, t_funct)
      # print(errors, sum(errors))
       ev, negative_gradient = bp(training_set[k], x_vals[k], weights)
       weights = update_weights(weights, negative_gradient, alpha)
    count += 1
    if(count == 100000): 
       weights = [[round(random.uniform(-2.0, 2.0), 2) for j in range(layer_counts[i]*layer_counts[i+1])]  for i in range(len(layer_counts)-1)]
       count = 0

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
   print(x_vals, errors)
   for k in range(len(training_set)):
      x_vals[k], errors[k] = ff(training_set[k], x_vals[k], weights, t_funct)
   # print(errors)
   # print(x_vals)
   #print([x_vals[a][-1] for a in range(len(x_vals))], errors)
   print (str(''.join([str(w)[1:-1] + '\n' for w in weights]))[:-2])# + str(training_set))
  # print (sum(errors))
if __name__ == '__main__': main()
# Dhruv Anurag 5 2024