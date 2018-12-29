# GA configuration settings

## How to use the configuration tool
GA uses a simple dictionary -> object attribute mapping function
meaning, any attribute the GA object holds, can be changed using this function.

```python
from PYGA import GA

LOCAL_GA = GA()

test_configuration = {
                    "generation_size": 1000,
                    "mutation_function": "roulette",
                    "max_score": 1000,
                    "iterate_evolution": True
                    }
                    
LOCAL_GA.configure(test_configuration)
```

Every setting and / or function meant for user-configuration can be found in this file.

### Selection Algorithms

```
GA.configure({"selection_function": " FUNCTION_NAME "})

- roulette:
    Roulette-wheel selection

```

### Mutation Algorithms

```
GA.configure({"mutation_function": " FUNCTION_NAME "})


- random_swap: 
    Randomly swaps two weights

- uniform: 
    Replaces the value of the chosen gene
    with a uniform random value between 0 and 1
```

### Crossover functions

```
GA.configure({"crossover_function": "FUNCTION_NAME"})

- mean_crossover:
    Uses the numpy.mean() values of each parent to create a new genome
```

### Miscellaneous 
```

- mutation_rate:
        # Integer describing the fractional percentge of new genomes
        # that will be mutated
        # mutation_rate = 7 means 1/7th of genomes will be mutated
        
- iterate_evolution:

        # True -> Yield every genome of every generation

        # False -> Return only the best Genome from the final generation

- generation_size: 
    How many genomes in each generation DEFAULT=100

- max_generations: 
    An upper boundary for the needed generations to stop evolution

- max_score: 
    An upper boundary for the needed score to stop evolution

- stagnation_hault: 
        
        # True -> Stops evolution once the fittest genome hasnt since the last generation
        
        # False -> Continues the evolution even if the resulting fitness value stagnates

- display_info:
        
        # True -> writes information about every generation and genome to stdout WARNING! substancially decreases effiency
                  However i would advocate trying it atleast once, to get a better understanding of what is happening.
        
        # False -> No additional information is printed
```
