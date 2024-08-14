
# Excape Sequences

#### Usage
`printf("There comes the newline\n")`

```
\n = newline
\t = tab (horizontal)
\v = vertical tab
\" = double quote
```

#### Variables
- ``int``
- ``float``
- ``char``
- ``char[]``

##### Call variables
| Type       | Callable | Name               |
| ---------- | -------- | ------------------ |
| ``int``    | ``%d``   | ``decimal``        |
| ``float``  | ``%f``   | ``float``          |
| ``char``   | ``%c``   | ``character``      |
| ``char[]`` | ``%s``   | ``array (string)`` |
The `char[]` variable is just an array of characters. Strings don't exist in C, because they are objects and C is not a object oriented language. 