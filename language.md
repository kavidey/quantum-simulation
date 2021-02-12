# Syntax
The first line of each program is the number of qubits to be used in in the program.

The following line can either be a number, or the first gate in the program. Normally the program outputs the probability of each possible output bit configuration, however, if the second line is a number, then it will simulate that many test runs, and return the total count of each output state.

A line can be turned into a comment by adding a `#` to the beginning. A comment _cannot_ start partway through a line.

Quantum gates can be run with the following syntax:
`gate_name gate_input_1 gate_input_2 ... gate_input_n`
# Quantum Gates
Several Quantum and Classical gates are available. This is the full list
| Command | Description | Input(s) | Example |
| ---: | --- | --- | --- |
| `NOT` | Basic NOT gate | The qubit index | `NOT 1` |
| `CNOT` | Basic CNOT gate | --- | `---` |
| `CCNOT` | Basic CCNOT gate | --- | `---` |
| `H` or `Hadamard` | --- | The qubit index | `H 0` |
| `ZNOT` | --- | --- | `---` |
| `OracleGA` | An oracle gate used in Grover's Algorithm | --- | `---` |
| `GroverDiffusion` | An diffusion gate used in Grover's Algorithm | --- | `---` |
| `HZn` or `HadamardOverZn` | --- | --- | `---` |
| `ADD` | --- | --- | `---` |
| `OracleSA` | An oracle gate used in Shor's Algorithm | --- | `---` |
| `Measure` | --- | The qubit index | `M 1` |
| `R` | --- | --- | `---` |

# Example Programs
## Superposition Example
``` python
1
2048

# Apply a Hadamard Gate to Qubit 0
H 0
# Measure qubit 0
M 0
```
This program should output `10` 50% of the time and `00` the other 50%
## Quantum Entanglement Example

``` python
2
2048

# Apply a Hadamard Gate to Qubit 0
H 0
# Entangle qubits 0 and 1
CNOT 0 1
# Measure both qbits
M 0
M 1
```