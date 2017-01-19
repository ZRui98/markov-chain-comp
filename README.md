# markov-chain-comp
Using Markov Chains and MIDIUtil to generate MIDI files

#Usage
If data is to be later added, the data is read in the format X,# X,#.... where X can be 0-127 for midi notes, and 128-132 for rests of length 1/16, 1/8, 1/4, 1,2, 1. \# is the octave from 0-10 if X is a midi note, otherwise # represents the index of the array [1/4,1/2,1,2,4]

#Todo
Add different length of midi notes
