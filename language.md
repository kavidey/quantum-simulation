# Syntax
The first line of each program is the number of qubits to be used in in the program.

The following line can either be a number, or the first gate in the program. Normally the program outputs the probability of each possible output bit configuration, however, if the second line is a number, then it will simulate that many test runs, and return the total count of each output state.

A line can be turned into a comment by adding a `#` to the beginning. A comment _cannot_ start partway through a line (i.e. after a command). It has to be on its own line

Quantum gates can be run with the following syntax:
`gate_name gate_input_1 gate_input_2 ... gate_input_n`
# Quantum Gates
Several Quantum and Classical gates are available. This is the full list
| Command | Description  | Example | Notes |
| ---: | --- | --- | --- |
| `NOT` | Basic NOT gate  `NOT 1` |
| `CNOT` | Basic CNOT gate | `CNOT 0 1` |
| `CCNOT` | Basic CCNOT gate | `CCNOT 0 1 2` |
| `H` or `Hadamard` | Puts a qubit in a superposition of 1 and 0 | `H 0` |
| `ZNOT` | Inverts the amplitude of all the qubits but the first one | `ZNOT` |
| `OracleGA` | An oracle gate used in Grover's Algorithm | `OracleGA` |
| `GD` or `GroverDiffusion` | An diffusion gate used in Grover's Algorithm | `GD` |
| `HZn` or `HadamardOverZn` | --- | `HZn 2` |
| `ADD` | --- | `ADD 3` |
| `OracleSA` | An oracle gate used in Shor's Algorithm | `OracleSA` |
| `R` | Rotates each qubit | `R 0.785398163397,-0.392699081699` | This gate is a bit weird, it requires one input per qubit, and the inputs are are comma separated rather than space separated |

# Example Programs
## Superposition Example
``` python
1
2048

# Apply a Hadamard Gate to Qubit 0
H 0
```
This program should output `1` 50% of the time and `0` the other 50%
## Quantum Entanglement Example

``` python
2
2048

# Apply a Hadamard Gate to Qubit 0
H 0
# Entangle qubits 0 and 1
CNOT 0 1
```
This program should output `11` 50% of the time and `00` the other 50%. Both bits are entangled, so they will always have the same value.

---

Sample programs for Grover's and Shor's algorithms are on the way!