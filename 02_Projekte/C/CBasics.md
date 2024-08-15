
# Escape Sequences

#### Usage
`printf("There comes the newline\n")`

```
\n = newline
\t = tab (horizontal)
\v = vertical tab
\" = double quotes
```

# Format Specifier %
- ``int``
- ``float``
- ``char``
- ``char[]``

#### Call variables
| Type       | Callable   | Name                 | Explanation                                                                               |
| ---------- | ---------- | -------------------- | ----------------------------------------------------------------------------------------- |
| ``int``    | ``%d``     | ``decimal``          | Stores whole numbers                                                                      |
| ``float``  | ``%f``     | ``float``            | Stores decimal numbers but is not precise                                                 |
| `double`   | `%lf`      | `double`             | Stores a lot more numbers and **more precise**                                            |
| ``char``   | ``%c, %d`` | `character, decimal` | You can convert it to a character using the asci table or just use it for numbers with %d |
| ``char[]`` | ``%s``     | ``string``           | Multiple characters attached to each other                                                |

The `char[]` type is just an array of characters. Strings don't exist in C, because they are objects and C is not a object oriented language. 

You would call a variable like that. 
```
#include <stdio.h>

int main(){
	int age = 23;

	printf("I am %d years old", age)

	return 0;
}
```

## Format Variables
Define what type of data has to be displayed. 

| Decimal Precision | Minimum field width | left align |
| ----------------- | ------------------- | ---------- |
| %.1               | %1                  | %-         |

Example:
```
	float Ware1 = 3.45;

    float Ware2 = 7.55;

    float Ware3 = 9.00;

    printf("Ware1: $%.4f\n", Ware1);

    printf("Ware2: $%-2.2f\n", Ware2);

    printf("Ware3: $%8.2f", Ware3);
```

Output:
```
Ware1: $3.4500 // displayed 4 numbers after the dot
Ware2: $7.55 // moved to the left
Ware3: $    9.00 // moved to the right 8 times
```

# Constants

#### Define a constant
```
    const float PI = 3.14159;

    printf("%f", PI);
```

# User Input

The classic function for user input is `scanf()`. 

Example with `scanf()`
```
#include <stdio.h>

int main(){
	int age;
	
	printf("How old are you?");
	scanf("%d", age);

	return 0;
}
```

The problem with `scanf()` is that it can't store white spaces. If you still want to implement a string with white spaces you should use `fgets()`. 

Example with `fgets()`:
```
#include <stdio.h>

int main(){
	char full_name[25];

	printf("What is you're full name?");
	fgets(full_name, 25, stdin) // stdin = standart input;

	printf("You're full name is %s", full_name);

	return 0;
}
```

When you execute this program you'll notice that a newline separates the sentence. That's because `fgets()` registered the enter key. It's a bit advanced to remove that newline but there is the code.

```
#include <stdio.h>

int main(){
	char full_name[25];

	printf("What is you're full name?");
	fgets(full_name, 25, stdin) // stdin = standart input;
	name[strlen(name)-1] = "\0";

	printf("You're full name is %s", full_name);

	return 0;
}
```

# Math
Here are some of the most used mathematical functions.
```
#include <stdio.h>

#include <math.h>

  

int main() {

  

    // special operations

    double SquareRoot = sqrt(64);

    int Round = round(5.673);

    int Round_Up = ceil(3.12);

    int Round_Down = floor(4.9);

  

    // classic operations

    float a = 5;

    float b = 7;

  

    float c = a + b;

  

    float d = b - a;

  

    float e = a * b;

  

    float f = a / b;

  

    printf("%.2f", f);

  

    return 0;

}
```

[Sourcecode](math_functions.c) 

# Functions
In C functions are important. The main function is called every time you wanna run a program. There is no program without a function. 

Exp. 
```
#include <stdio.h>

int main()
{
	printf("This is the main function.");

	return 0;
}
```

We can also create custom functions. That would work like that.

```
#include <stdio.h>

void custom_function()
{
	printf("This is a custom function.");
}

int main()
{
	printf("This is still the main function.");

	return 0;
}
```

