from qiskit import QuantumCircuit,execute,BasicAer
import random
import pygame

n = 4
qc = QuantumCircuit(n+1, n)
nQc = QuantumCircuit(n+1)
pygame.init()

# Audio Files
hGate = pygame.mixer.Sound("aNote.wav")
xGate = pygame.mixer.Sound("bNote.wav")
cxGate = pygame.mixer.Sound("cNote.wav")
idGate = pygame.mixer.Sound("dNote.wav")
zGate = pygame.mixer.Sound("eNote.wav")
measure = pygame.mixer.Sound("gNote.wav")

# List Creation
firstQubit = []
secondQubit = []
thirdQubit = []
fourthQubit = []
AncillaQubit = []

# Check Qubits function to assign gates
def checkQubit(index):

    if index == 0:  
        qubit_seq = firstQubit
    elif index == 1:
        qubit_seq = secondQubit
    elif index == 2:
        qubit_seq = thirdQubit
    elif index == 3:
        qubit_seq = fourthQubit
    elif index == 4:
        qubit_seq = AncillaQubit
    
    
    # Checks for phase-kickback
    i = 0
    while i < len(qubit_seq) - 2:
        if qubit_seq[i:i+3] == ['h', 'cx', 'h']:
            qubit_seq[i:i+3] = ['z']
        i += 1
       
    return qubit_seq



def constant(qc):
    for i in range(n):
        qc.id(i)
        checkQubit(i).append("id")



def balanced(qc):
    for i in range(n):
        qc.cx(i,n)
        checkQubit(i).append("cx")

        

def deutshJozsha(qc):
    out1 = ''
    out0 = ''
    functions = [1, 0]
    for i in range(n):
        qc.h(i)
        checkQubit(i).append("h")
    qc.x(n)
    checkQubit(4).append("x")
    qc.h(n)   
    
    checkQubit(4).append("h")

    v = random.choice(functions)
    qc.barrier()
    if v == 1:
        balanced(qc)
    if v == 0: 
        constant(qc)
    
    for i in range(n):
        qc.h(i)
        checkQubit(i).append("h")
        out1 += '1'
        out0 += '0'
        
    qc.barrier()
    
    for i in range(n):
        qc.measure(i, i)
        checkQubit(i).append("m")

    print(qc.draw("mpl"))
    job = execute(qc, BasicAer.get_backend('statevector_simulator'))
    output = job.result().get_counts()
    v = list(output.keys())[0]
    print(output)
    if v == out1:
        print("balenced")
    elif v == out0:
        print("constent")
        

 
def playCircuit(qc, s):
    for i in range(len(s)):
        if s[i] == "h":
            hGate.play()
            qc.h(0)
        elif s[i] == "x":
            xGate.play()
            qc.x(0)
        elif s[i] == "cx":
            cxGate.play()
            qc.cx(0,1)
        elif s[i] == "id":
            idGate.play()
            qc.id(0)
        elif s[i] == "z":
            zGate.play()
            qc.z(0)
        elif s[i] == "m":
            measure.play()
            qc.measure(0, 0)
        
        pygame.time.delay(int(hGate.get_length() * 20) * len(s))


    
deutshJozsha(qc)    

circuit = firstQubit + secondQubit + thirdQubit + fourthQubit 

# Print results
print("Qubit[0]:", firstQubit)
print("Qubit[1]:", secondQubit)
print("Qubit[2]:", thirdQubit)
print("Qubit[3]:", fourthQubit)
print("Ancilla Qubit:", AncillaQubit)

# Transpose of lists
transposed_list = list(zip(firstQubit, secondQubit, thirdQubit, fourthQubit))

# Flatten transposed list
flat_list = [gate for sublist in transposed_list for gate in sublist]

# Execution
playCircuit(qc, flat_list)
print(flat_list)
