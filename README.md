## Coding Style

- Always add space between binary operators. Such as "+, -, *, etc."

- No space between numbers and unary operators. For example:

- Add space between for, if and the parentheses.
```js
const numberArr = [1, 2, 3];
for (let idx = 0; i < numberArr.length; i++) // good
for(let idx = 0; i < numberArr.length; i ++) // bad
```


- Use single blank lines to separate coding blocks with different logic.

- Always add a space after a comma operator.

## Readability

- Use one to two words to describe a function name or a variable.

- Within a single function, avoid having more than three levels of indentation. If this occurs, employ helper functions to streamline the logic.

- In python, more continue, less if, less else statement. 
```python
for ...:
    if condition1:
        do something
        if condition2:
            do something
            do something
            do something
            do something
            do something
            do something

# instead:
for ...:
    if not condition1:
        continue
    do something
    if not condition2:
        continue
    do something
    do something
    do something
    do something
    do something
    do something
```

## Bug Free

- ALWAYS consider and check for edge cases.

- When accessing an element's position within a collection (such as arrays or matrices), always ensure the subscript (position, index) does not exceed the boundaries.

- NO global variable.