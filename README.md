# Quantum-Orchestra

# Overview:

The main objective of the project is to produce music using quantum concepts to create different
musical notes and to mimic the music composer.

# Tools Used: 

Libraries and Frameworks: 
Qiskit, Pygame, Threading, Flask.

Programming Languages:
Python, CSS, html.

# Logic Explained:

At first, we linked each gate to a note and created a list of each Quibit to fill it with the gates based on the algorithm being played.

We have created a function that checks the index and links it to a qubit list.

We have tested our logic by implementing two algorithms, the Deutsch–Jozsa algorithm and the Superdense algorithm, each algorithm introduces a special case.

In Deutsch–Jozsa algorithm, we have the phase kickback special case which mimics the z gate, and having a couple of phase kickbacks made us hear the note in a unique way.

In the Superdense algorithm, we have the bell states which are the entangled states, in the entanglement the qubits affect each other which is why we hear a duplication of notes, in addition to that, the entanglement have a unique note that will continue playing till the disentanglement happens,  and this could happen because of the implementation of the threading library, which is why we can run two notes concurrently.

It is important to mention that we have applied a block of code for the transpose, to make the reading vertical and not horizontal just like the music theory.

We printed the qubits with the gates associated with it, to ensure that each gate is being inserted into each list and being played as well.

We have created a function to play the algorithm, which also indicates the period of time between each note and another, to make the overall symphony either short or long.
