# Efficient generation of justifications for collective decision making
This code has been implemented for: Bachelor Thesis Efficient Generation of Justifications for Collective Decision Making

### Implemented axioms:
1. Pareto principle
2. Condorcet principle
3. Faithulness
4. Cancellation
5. Neutrality
6. Anonymity

#### This code uses the packages numpy and pylgl; please run `pip install -r requirements.txt` or `pip3 install -r requirements.txt` before running the code

### Two algorithms have been implemented:
1. Algorithm to generate justifications based on axioms that refer to one profile (axiom 1 until 4).
#### How to run:
`python3 oneProfile.py`
2. Algorithm to generate justifications based on axioms that refer to at most two profiles (axioms 1 until 6). 
#### How to run:
`python3 twoProfile.py`

In both files the target profile and target outcome can be changed as well as the axioms in the normative basis.
