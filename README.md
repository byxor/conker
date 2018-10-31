# conker
Contracts for python

## Install

```
pip install conker
```

## Examples

```python
import math
from conker import pre


@pre("n > 0")
def square_root(n):
    return math.sqrt(n)


print(square_root(16)) # 4
print(square_root(9))  # 3
print(square_root(4))  # 2
print(square_root(1))  # 1
print(square_root(0))  # 0
print(square_root(-1)) # raises ConkerError
```
