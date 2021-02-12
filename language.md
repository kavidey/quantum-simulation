# Syntax
The first line of each program is a single number: the number of Qubits needed for the program. This number is taken to the power of 2, so 2 would be 4, 5 would be 32, etc.

The following line can either be a number, or the first gate in the program. Normally the program outputs the probability of each possible output bit configuration, however, if the second line is a number, then it will simulate that many test runs, and return the total count of each output state.

The first Qubit is autmatically set to one.

Quantum gates can be run with the following syntax:

`gate_name gate_input_1 gate_input_2 ... gate_input_n`
# Quantum Gates
Several Quantum and Classical gates are available. This is the full list
| Command | Description | Input(s) | Example |
| ---: | --- | --- | --- |
| `NOT` | --- | The qubit index | `NOT 1` |
| `CNOT` | --- | --- | `---` |
| `CCNOT` | --- | --- | `---` |
| `H` or `Hadamard` | --- | The qubit index | `H 0` |
| `ZNOT` | --- | --- | `---` |
| `OracleGA` | --- | --- | `---` |
| `GroverDiffusion` | --- | --- | `---` |
| `HZn` or `HadamardOverZn` | --- | --- | `---` |
| `ADD` | --- | --- | `---` |
| `Oracle SA` | --- | --- | `---` |
| `Measure` | --- | The qubit index | `M 1` |
| `R` | --- | --- | `---` |

# Example Programs