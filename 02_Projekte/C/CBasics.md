
# Excape Sequences

#### Usage
`printf("There comes the newline\n")`

```
\n = newline
\t = tab (horizontal)
\v = vertical tab
\" = double quotes
```

#### Variables
- ``int``
- ``float``
- ``char``
- ``char[]``

##### Call variables
| Type       | Callable   | Name                 | Explanation                                                                               |
| ---------- | ---------- | -------------------- | ----------------------------------------------------------------------------------------- |
| ``int``    | ``%d``     | ``decimal``          | Stores whole numbers                                                                      |
| ``float``  | ``%f``     | ``float``            | Stores decimal numbers but is not precise                                                 |
| `double`   | `%lf`      | `double`             | Stores a lot more numbers and **more precise**                                            |
| ``char``   | ``%c, %d`` | `character, decimal` | You can convert it to a character using the asci table or just use it for numbers with %d |
| ``char[]`` | ``%s``     | ``array (string)``   | A list of variables                                                                       |

The `char[]` type is just an array of characters. Strings don't exist in C, because they are objects and C is not a object oriented language. 