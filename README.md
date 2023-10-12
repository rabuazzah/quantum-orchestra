# quantum-orchestra

####Description of the code of the project

Quantum Orchestra

Overview:

The project is called Quantum Orchestra, the main objective of the project is 
to produce music using quantum and implement quantum concepts to create different
musical notes.

Tools Used: 

The libraries that we needed were Pygame, which made us able to play the sounds of the notes, and we used flask, to be able to inject the frontend (html, css) code to the 
original backend code.

Logic Explained:

At first, we have linked each gate to a note, and created a list of each Quibit to fill it with the gates based on the algorithm being played.

We have created a function that checks the index, and link each index to a qubit list.

We have tested our logic by implementing two algorithms, Deutsch Jozsa and Superdense algorithm, each algorithm introduce a special case.

In Deutch Jozsa algorithm, we have the phase kickback special case which we presented as the Z note, which is linked to the Z gate, which makes us hear it in a unique way.

In Superdense algorithm, we have the bell states which are the entangled states, in entanglement the qubits affect each other that’s why we hear a duplication of notes, in addition to that, the entanglement got a unique note that will continue playing till the disentanglement happens,  and this could happen because of the implementation of the threading library, which can run two notes concurrently.

It is important to mention that we have applied a block of code for the transpose, to make the reading vertical and not horizonital just like the music theory and also we have imported shredding library which makes us able to run audio concurrently.

We printed the gates along with the Qubits its linked to, to proof that it is being inserted into each list and being played as well.

We have created a function to play the algorithm, which indicates the period of time between a note and another, which makes the overall symphony either short or long.
