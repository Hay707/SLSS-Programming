# Syntax Errors

These type of errors are ones that occur when you run your code and then it breaks.

Syntax errors are relatively easy to `spot` and `fix`

Syntax errors occur when we don't follow the rules of the language completely.

# Semantics Errors

Semantic errors occur when our coed doesn't MEAN what we intend it to MEAN
It's all about the "MEANING"behind the code

These errors, in Mr. Ubial's opinion, are FAR MORE challenging to spot and fix

```python
user_response = input("Do you like to eat food?")

if user_response == "yes": 
	print("You are a human :)")
else: 
    print("You must be some sort of robot")
```

The problem with the code above is subtle. What I (the writer) mean is that EVERY ANSWER OF YES should go into the YES block.