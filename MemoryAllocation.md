## Stack space 
- When a program is running, the operating system allocates a fixed amount of memory to a process so it can carry out functions like function calls, recursion, and other operations without interference from other processes. This memory is a specific size, for example, 8MB. The size isn't too large, as making it too big would lead to inefficient memory utilization. This allocated memory is what we refer to as the 'stack space' or 'Stack space'."

- Stack space primarily contains the following components: 1) Function arguments and return values. 2) Local variables of the function".

- The content stored in the stack space will be cleaned up once the function execution ends.

## Stack Overflow 
What we commonly refer to as a 'stack overflow' happens when, during function calls or recursive calls, too much memory is allocated, exceeding the small fixed space that the operating system has reserved. 

## Example

```py
def f(n):
    nums = [0]*n  
    sum = 0
    for i in range(n):
        nums[i] = i
        sum += i
    return sum
```

```java
public int f(int n) {
    int[] nums = new int[n];
    int sum = 0;
    for (int i = 0; i < n; i++) {
        nums[i] = i;
        sum += i;
    }
    return sum;
}
```

In the above examples, **the parameter n**, **the return value of the function f**, and **the local variable sum** are all easily identified as being stored in the stack space. 

The main point of confusion or complexity here is with nums.

Here, nums can be understood in two parts:

- A local variable named nums, which holds a reference to a memory location. This address is typically 4 bytes (for a computer with a 32-bit address bus, the address size is 4 bytes).
- An integer array, int[n], that's been allocated with n positions. This occupies 4×n bytes in total.
- The variable nums itself is stored in the stack space since it's a local variable. However, the 
n integers stored within nums are stored in the **heap space, or 'Heap space'**. They do not occupy the stack space, hence they won't lead to a stack overflow.
- The local variable nums will be garbage collected once the function excution ends.

In most programming languages, especially in languages like Java and Python, almost everything is an object. Practically every variable has both its own value and the memory space it points to, in terms of its logical meaning."

<div style="border:1px solid red;padding:10px;">
    <strong>Note: This is important note</strong> <br />
    I previously believed that in Python, everything is a class rather than an object. This appears contradictory to the assertion that in both Java and Python, almost everything is an object. Let me clarify this perspective.
    <ul>
    <li>
        Everything in Python is an object (since everything is an instance of some class)
    </li>
    <li>
        Python's model is <strong>class-based</strong>, as we define behavior and structure through classes
    </li>
    </ul>
    <p>
    In Python, everything is indeed an object. When we say "everything is an object," we mean that everything, from numbers to lists to functions, is an instance of a class and therefore an object. Even the classes themselves are objects!
    </p>
    <p>
    However, Python's object model is class-based: when we define classes, and we create objects as instances of these classes. The classes define the properties and behaviors that their instances (or objects) will have.
    </p>
</div>