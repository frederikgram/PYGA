# PYGA - NOT DONE / NAME NOT FOUND
Dynamically implement weight tweaking using Genetic Algorithms 
into your project via. simple stdio communication

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PYGA. // NOT AVAILABLE

```bash
pip install PYGA 
```

## Usage

Read the [configuration guide](configuration_guide.md) thoroughly before using the framework, otherwise it will be
difficult to configure the framework so it works for your specific application

### Initialization

```python
# Imports
from PYGA import interface

# Required
interface.n_features = 10 # How many features will your application use?

# Optionals
interface.max_score = 1000 #  stop at n fitness score
interface.max_generation = 50 #  stop at n generation

interface.stagnation_hault = False # If False, the evolution will keep going
                                   # even if population fitness stagnates

interface.iterate_evolution = True # Yield every generation as a list of Genomes
                                   # if False, return the fittest Genome at the end of the evolution

```
### Evolution
Take a simple pong game as an example, where a computer plays by itself,
 against a wall. And its movements (up or down) is to be determined by a set of features.
In this case you would simply:
1) write a set of features to stdout before the game starts
2) read a list of weights from stdin
3) start the game and play using the weights 
4) write the score to stdout at the end of the game.
5) Repeat from 2.

Once the evolution is completed either by hitting custom evolutionary bounds or stagnation,
a <complete> tag followed by a list of the highest scoring weights will be written to stdout PYGA

// Example code can be found in the Examples/pong folder

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
Just use it

## Project status
Testing stage