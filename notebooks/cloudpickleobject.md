
I've been using `cloudpickle` in the internals of [taskloaf](https://github.com/tbenthompson/taskloaf) for a while since it allows serializing almost all functions and objects. That's really nice since it means I can pass arbitrary functions (tasks, jobs) from one worker to another across the network.

Yesterday, I was curious about the internals of `cloudpickle` and whether a monkey-patched object would remain patched after being loaded remotely. I read a bit of the source, but figured just trying it was a good idea.

I create a silly, meaningless class and then an instance of that class.


```python
# Create a silly class and an object
class Turkey:
    def hi(self):
        return "hello"
t = Turkey()
print(t.hi())
```

    hello


Then, I monkey patch the `hi` method to return 1 instead of 2. `types.MethodType` turns a free-standing function into a method that automatically receives the `self` parameter.


```python
import types
def hi2(self):
    return "SQUAWK"
t.hi = types.MethodType(hi2, t)
print(t.hi())
```

    SQUAWK


First, I'll try `pickle`. I dump the turkey to a binary blob and reload it.


```python
import pickle
blob = pickle.dumps(t)
t2 = pickle.loads(blob)
print(t2)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-3-21cb01513bb4> in <module>()
          1 import pickle
          2 blob = pickle.dumps(t)
    ----> 3 t2 = pickle.loads(blob)
          4 print(t2)


    AttributeError: 'Turkey' object has no attribute 'hi2'


`pickle` serialize a reference to the the type of the object and then expects that type to provide all the member functions needed. So, it's not able to handle this monkey patching situation.

Next, I'll try `cloudpickle`!


```python
import cloudpickle
t2 = cloudpickle.loads(cloudpickle.dumps(t))
print(t is t2)
```

    False


Does the `hi` method remain changed? YES! Thank you, cloudpickle. 


```python
print(t2.hi())
```

    SQUAWK


Ultimately, this makes a lot of sense. `cloudpickle` just investigates the members of an object (its `__dict__`) and serializes those. It doesn't need to serialize anything about the generic `Turkey` class. The key difference with `pickle` is that `cloudpickle` has the capability to serialize functions and so it can directly serialize members of the object without reference to its type.
