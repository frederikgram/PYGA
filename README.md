# PYGA
Dynamically implement weight tweaking via. Genetic Algorithms 
into your project.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PYGA. // NOT AVAILABLE

```bash
pip install PYGA 
```

## Usage

Read the [configuration guide](configuration_guide.md) thoroughly before using the framework, otherwise it will be
difficult to configure the framework so it works for your specific application

### Fast evolution
Sometimes for a project, we do not care about the inbetween steps, we just want an answer and we want it _now_
for this exact reason, the PYGA GA can also be used as a simple return function.
in the [configuration guide](configuration_guide.md) it is shown how to set iterate_evolution.

The list of weights that is returned, is the fittest genome of the newest generation. Meaning that 
older and potentially better solutions _could_ get lost. 

Below is an example of how to use PYGA as a simple return function.
```
from PYGA import GA #  First we import our GA like so
import numpy as np

TEST_CONFIGURATION = {          #  Here we createa a simple configuration,
    "generation_size": 100,     #  Notably, iterate_evolution is set to False
    "iterate_evolution": False,
    "max_fitness": 0.80,
}


def asses_fitness(weights: list) -> float:   #  gives a fitness score based on the mean of the weights
    """ Higher weights give higher fitness """
    return np.mean(weights)

# Initialize a GA, with 5 weights and fitness assesment function
LOCAL_GA = GA(_num_weights=5, fitness_function=asses_fitness)  

# Apply configuration
LOCAL_GA.configure(TEST_CONFIGURATION)          

# Fast evolve
fittest_weight = LOCAL_GA.evolve():

print(fittest_weight)

""" As shown, we simply set a variable to be equal to
    the return of GA.evolve()
    
    this return has type list[float] 
"""
```


### Iterative evolution
In some projects, especially projects like teaching, the ability to visualize the evolution is necessary.
because of this, PYGA is developed so it works both iteratively or as a simple return-function.

as seen in the [configuration guide](configuration_guide.md) you simply set iterate_evolution to be True
to enable this feature.

Below is an example of how to use PYGA for iterative evolution, 
the example simply gives a score based on the mean of the weights (higher is better)

```
from PYGA import GA #  First we import our GA like so
import numpy as np

TEST_CONFIGURATION = {          #  Here we createa a simple configuration,
    "generation_size": 100,     #  Notably, iterate_evolution is set to True
    "iterate_evolution": True,
    "max_fitness": 0.99,
    "display_info": False,
}


def asses_fitness(weights: list) -> float:   #  gives a fitness score based on the mean of the weights
    """ Higher weights give higher fitness """
    return np.mean(weights)

# Initialize a GA, with 5 weights and fitness assesment function
LOCAL_GA = GA(_num_weights=5, fitness_function=asses_fitness)  

# Apply configuration
LOCAL_GA.configure(TEST_CONFIGURATION)          

# Start Evolution
for iteration in LOCAL_GA.evolve():
    """ We can simply use GA.evolve() as a generator function, that yields
        every single weight / genome that gets created.
        
        if you want to seperete generation from eachother,
        just split at generation_size num of iterations.
    """
    
    print(iteration)

```

## Examples
Example code can currently be found in /tests/test_ga.py

## Contributing

Crossover, Mutation and Selection.py are all welcome to new additions.
If a new algorithm / function is added, please add it to the configuration_guide.md and 
explain what it does.


Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
Just use it

## Project status
Barely workin'