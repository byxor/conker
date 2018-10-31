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


print(square_root(16)) # prints '4'
print(square_root(9))  # prints '3'
print(square_root(4))  # prints '2'
print(square_root(1))  # prints '1'
print(square_root(0))  # prints '0'
print(square_root(-1)) # raises ConkerError
```

```python
@pre(
    "isinstance('account', Account)",
    "isinstance('reason', str)",
    "isinstance('duration_in_hours', (int, float))",
    "duration_in_hours > 0",
)
def ban(account, reason, duration_in_hours):
    pass
```
