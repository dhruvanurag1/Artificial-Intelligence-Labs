import sys; args = sys.argv[1:]
file = open(args[0], 'r')
import math

def transfer(t_funct, input):
    if t_funct == 'T1': return input
    if t_funct == 'T2': return max(0, input)
    if t_funct == 'T3': return 1/(1+math.exp(-input))
    if t_funct == 'T4': return -1 + (2/(1+math.exp(-input)))
    
def dot_product(input, weights, stage):
    return sum(input[i] * weights[i] for i in range(len(weights)))

def evaluate(file, input_vals, t_funct):
    file = list(file)
    for a in range(len(file)): file[a] = file[a].strip().split()
    new_weights, temp_vals = input_vals, input_vals
    for c in file:
        if c != file[-1]:
            new_list = [[float(a) for a in c[x:x+len(temp_vals)]] for x in range(0, len(c), len(temp_vals))]
            new_weights = [0] * len(new_list)
            for a in range(len(new_list)): new_weights[a] = transfer(t_funct, dot_product(temp_vals, new_list[a], "stage"))
            temp_vals = new_weights
        else:
            temp_vals = [temp_vals[a] * float(c[a]) for a in range(len(c))]
    return temp_vals
    

def main():
    inputs, t_funct, transfer_found = [], 'T1', False
    for arg in args[1:]:
        if not transfer_found:
            t_funct, transfer_found = arg, True
        else:
            inputs.append(float(arg))
    print(inputs)
    li = (evaluate(file, inputs, t_funct))
    for x in li:
        print(x, end = ' ')
if __name__ == "__main__": main()

#Dhruv Anurag 5 2024