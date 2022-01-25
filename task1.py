cpu_dictionary={}
mem_dictionary={}
def write_to_dictionary(line):
    values=line.split()
    if values[0] not in cpu_dictionary:
        cpu_dictionary[values[0]]=[]
    cpu_dictionary[values[0]].append(int(values[1]))
    if values[0] not in mem_dictionary:
        mem_dictionary[values[0]]=[]
    mem_dictionary[values[0]].append(int(values[2]))
def file_reader():
    file=open("input1.txt","r")
    for i,line in enumerate(file):
        if(i==0):
            continue
        write_to_dictionary(line)
    file.close()
file_reader()
def get_maximum(dictionary):
    cpu_max=0
    max_dictionary={}
    for dict in dictionary:
        max_dictionary[dict]=max(dictionary[dict])
    return max_dictionary
def write_to_file(cpu_max_dictionary, mem_max_dictionary):
    header="NAME_OF_POD    MAX_CPU    MAX_MEM"
    with open('result1.txt', 'w') as f:
        f.write(header + "\n")
        for x in cpu_max_dictionary:
            f.write(str(x) + " " + str(cpu_max_dictionary[x]) + "          " + str(mem_max_dictionary[x])+ "\n")
        f.close()
cpu_max_dictionary=get_maximum(cpu_dictionary)
mem_max_dictionary=get_maximum(mem_dictionary)
write_to_file(cpu_max_dictionary,mem_max_dictionary)


