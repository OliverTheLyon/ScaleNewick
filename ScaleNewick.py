import sys


file_name = sys.argv[1]
factor = float(sys.argv[2])
out_file = sys.argv[3]

f = open(file_name, "r")
string = f.read()
f.close()

new_tree = ""
temp = ""
branch_sum = 0.0
in_length = False
for ch in string:
    if(ch == ':'):
        in_length = True
        new_tree += ':'
        continue
    elif(ch not in "0123456789." and in_length):
        in_length = False
        x = float(temp) * factor
        new_tree += str(x)
        branch_sum += x
        temp = ""
        new_tree += ch
        continue
    if(in_length):
        temp += ch
    else:
        new_tree += ch

f = open(out_file, "w")
f.write(new_tree)
f.close()
