from qiskit import QuantumCircuit, Aer, execute
import pygame
import threading

# Audio Files

pygame.init()
hGate = pygame.mixer.Sound("aNote.wav")
xGate = pygame.mixer.Sound("bNote.wav")
cxGate = pygame.mixer.Sound("cNote.wav")
idGate = pygame.mixer.Sound("dNote.wav")
zGate = pygame.mixer.Sound("eNote.wav")
measure = pygame.mixer.Sound("gNote.wav")
entag = pygame.mixer.Sound("entang.wav")
disentag = pygame.mixer.Sound("disentang.wav")

stop_entag = False

# List Creation

firstQibit = []
secondQibit = []

# Check Qbit Function

def checkQbit(index):
    if index == 0:  
        return firstQibit
    elif index == 1:
        return secondQibit
    

# Superdense Code is a quantum communication protocol to communiate a number of classical bits of information by only transmitting a smaller number of qubits.

# Superdense coding depends on the entanglement concept, it is when multiple objects share a single quantum state, in other words, it is the affect of one qubit on another, and we have four entanglement states known as bell states.

qb = QuantumCircuit(2, 2)

def Ebit(qb):
    qb.h(0)
    checkQbit(0).append("h")
    qb.cx(0, 1)
    checkQbit(0).append("cx")

def message(qb, userInput):
    
    if userInput == "11":
        qb.id(0)
        checkQbit(0).append("id")
        
    elif userInput == "00":
        qb.x(0)
        checkQbit(0).append("x")
        qb.z(0)
        checkQbit(0).append("z")
        
    elif userInput == "01":
        qb.x(0)

        checkQbit(0).append("x")
       

    elif userInput == "10":
        qb.z(0)
        checkQbit(0).append("z")

def decoding(qb):
    qb.cx(0, 1)
    checkQbit(0).append("cx")
    qb.h(0)
    checkQbit(0).append("h")

def superdense(qb):
    Ebit(qb)
    userInput =  input("enter the message: ")
    message(qb, userInput)
    
    decoding(qb)
    
    qb.measure(0, 0)
    checkQbit(0).append("m")
    qb.measure(1, 1)
    checkQbit(1).append("m")
    
    # Execute the circuit
    
    job = execute(qb, Aer.get_backend('qasm_simulator'),shots = 1000)
    print(job.result().get_counts())
    
superdense(qb)

# Entanglement function

def entag_loop():
    global stop_entag
    while not stop_entag:
        entag.play()
        pygame.time.delay(int(entag.get_length() * 1000))  

# Play Circuit Function

def playCircuit(s):
    global stop_entag

    played_gates = []   
    entangled = False
    
    i = 0
    
    while i < len(s):
        # Check for entanglement
        
        if s[i] == "h" and s[i+1] == "cx":

            stop_entag = False
            threading.Thread(target=entag_loop).start() # Continuously playing entanglement note
            played_gates.append("entag")   
            entangled = True
            i += 2
            continue
        
        # Check for disentanglement
        if s[i] == "cx" and s[i+1] == "h":
            stop_entag = True  # Stop the entaglement sound loop
            disentag.play()   
            played_gates.append("disentag")   
            entangled = False
            i += 2
            continue
        
        if entangled:
            
            # Duplicates operations within the entanglement
            
            if s[i] == "x":
                xGate.play()
                played_gates.append("x")
                
                pygame.time.delay(int(xGate.get_length() * 1000))

                xGate.play()
                played_gates.append("x")  


                
            elif s[i] == "z":
                zGate.play()   
                played_gates.append("z")  

                pygame.time.delay(int(zGate.get_length() * 1000))
                
                zGate.play()  
                played_gates.append("z")  
        
            elif s[i] == "id":
                idGate.play()   
                played_gates.append("id")  

                pygame.time.delay(int(zGate.get_length() * 1000))
                
                idGate.play()
                played_gates.append("id")  

            
        else:
            if s[i] == "h":
                hGate.play()   
                played_gates.append("h")
                
            elif s[i] == "x":
                xGate.play()   
                played_gates.append("x")
                
            elif s[i] == "cx":
                cxGate.play()  
                played_gates.append("cx")
                
            elif s[i] == "id":
                idGate.play()   
                played_gates.append("id")
                
            elif s[i] == "z":
                zGate.play()   
                played_gates.append("z")
            
            elif s[i] == "m":
                measure.play()   
                played_gates.append("m")
                
        i += 1
        pygame.time.delay(int(hGate.get_length() * 1500))  



    # Ensure the entag sound stops at the end, in case the loop finishes while still entangled
    
    stop_entag = True
    return played_gates


# Create a circuit that contains both quibits and their values

s = firstQibit + secondQibit
played_gates_output = playCircuit(s)


# Print the gates added to each qubit and play the notes

qb.draw("mpl")
print(f"Qbitp[0] => {firstQibit}\nQbitp[1] => {secondQibit}") 
print(played_gates_output)

