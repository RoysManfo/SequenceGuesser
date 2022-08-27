# SeGu.brain : The brain of SeGu AI (Sequence Guesser Artificial intelligence)
__Each time SeGu AI guesses the correlation between numbers, its brain signs this correlation,
which will be used as a starting point for next challenges.__

__Exaples:__

```
SeGu AI guesses that the correlation between the numbers [1, 2, 3, 4, 5] is +1, its brain signs +1.
```

```
SeGu AI guesses that the correlation between the numbers [0, 2, 4, 6, 8] is +2, its brain signs +2.
```

```
SeGu AI guesses that the correlation between the numbers [1,3,5,7,9] is 2, its brain DOESN'T sign again 2.
```

```
SeGu AI guesses that the correlation between the numbers [0, 3, 6, 9, 12] is 2.5, wrong, its brain DOESN't sign 2.5.
```
___
## How does it work ?
Each time SeGu AI guesses the correlation between numbers, its brain signs this correlation which will be used as a starting point for the next challenges. In this way, SeGu AI can learn how to guess the correlation between numbers.

When a correlation is by addiction, SeGu AI will write on it's brain "x + _the number of the correlation_".
```
Array: [1, 2, 3, 4, 5]                Correlation: +1     Brain: x + 1
Array: [0, 2, 4, 6, 8]                Correlation: +2     Brain: x + 2
Array: [1, 2.5, 4, 5.5, 7]            Correlation: +1.5   Brain: x + 1.5
```
And so on.

When a correlation is by subtraction, SeGu AI will write on it's brain "x - _the number of the correlation_".
```
Array : [10, 9, 8, 7, 6]              Correlation: -1     Brain: x - 1
Array : [11, 9, 7, 5, 3]              Correlation: -2     Brain: x - 2
Array : [7, 5.5, 4, 2.5, 1]           Correlation: -1.5   Brain: x - 1.5
```
And so on.

Same thing with multiplication, SeGu AI will write on it's brain "x * _the number of the correlation_".
```
Array: [1, 2, 4, 6, 8]                 Correlation: *2     Brain: x * 2
Array: [1, 3, 6, 9, 12]                Correlation: *3     Brain: x * 3
Array: [11, 121, 1331, 14641, 161051]  Correlation: *11    Brain: x * 11
```
And so on.

When a correlation is by division, SeGu AI will write on it's brain "x / _the number of the correlation_".
```
Array: [64, 32, 16, 8, 4]               Correlation: /2     Brain: x / 2
Array: [27, 24, 21, 18, 15]             Correlation: /3     Brain: x / 3
Array: [161051, 14641, 1331, 121, 11]   Correlation: /11    Brain: x / 11
```
___
## Syntax
To remember what SeGu AI lerrned, it will call the function "__remember( )__" wich will read the brain and start interpreting what's written to give a result.

A cell is usualy written like this:
```
x [sign of the operation] [correltion] 
```
For example, something like
```
x + 5 
```
Will be interpreted like:  
"_To get the next number, I need to add 5 to the last number of the sequence_" ( x = y + 5 )
___
## Special cases

In some situations the equation could be more complex, and involve multiple previuos numbers.  
In that case, the syntax will use "x1, x2, x3 ..."
where x1 is the last number of the sequence, x2 is 
the second to last and so on.  

x0 will not be used in the brain, but you can still think about it as "_the number I'm trying to guess_"