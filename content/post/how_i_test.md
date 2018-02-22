+++
title="My Python testing set up"
date=2018-02-22
+++

To follow up on the last post about testing for science and data analytics, I thought it'd be nice to talk about the specific tools I use for testing. I don't claim this is the best way to do things, but it tends to work pretty well for small projects and teams.

## py.test
The py.test tool is handy for running a suite of tests in python. It's a very general tool for running all the tests in a project. It can do a lot of powerful things, but requires almost no boilerplate to get started with. The pattern I've always followed is: Add a `tests` directory the root of the project. Name any test files in that directory `test_xyz.py` and then any tests within that file `def test_abc():`. py.test will find all of these automatically and run them. On several projects that I work on, I have tens or hundreds of tests that, in total, take less than a second to run. As a result, I simply run `py.test` every time I make a change.

For more happiness, I add a `pytest.ini` file to the root of my project:

```
[pytest]
addopts = -s --tb=short
```

The `-s` causes any text printed by my tests or code to appear on the screen. By default, py.test suppresses printing/logging to standard out. Personally, I don't like that while debugging.
The `--tb=short` leads to shorter, more concise tracebacks in the case of test failures. 

There are a ton of other features available with py.test, like fixtures, fancy assertions and lots of plugins. Here's [a more comprehensive intro to py.test](http://pythontesting.net/framework/pytest/pytest-introduction/)

## Golden master tests

Golden master testing doesn't really **require** any special infrastructure, but it can be nice to have a coordinated way to generate the keys and specify golden master tests. First, I set up a configuration option in `tests/conftest.py`. This is a special file that `py.test` uses to load plugins and configuration.

```
def pytest_addoption(parser):
    parser.addoption(
        "--save-golden-masters", action="store_true",
        help="reset golden master benchmarks"
    )
```

Then, what you do with this depends on the project. In one project, where I'm normally compare numpy arrays, I have a decorator that makes setting up a golden master test really simple.

```
def golden_master(digits = 6):
    def decorator(test_fnc):
        try:
            save = pytest.config.getoption("--save-golden-masters")
        except AttributeError as e:
            save = False
        @wraps(test_fnc)
        def wrapper(request, *args, **kwargs):
            result = test_fnc(request, *args, **kwargs)
            test_name = request.node.name
            filename = os.path.join('tests', 'golden_masters', test_name + '.npy')
            if save:
                np.save(filename, result)
            correct = np.load(filename)
            np.testing.assert_almost_equal(result, correct, digits)
        return wrapper
    return decorator
```

To use this:

```
@golden_master(4)
def test_mycomplexfnc(request):
    return mycomplexfnc()
```

When I run `py.test --save-golden-masters`, this will automatically save the result of the function to `tests/golden_masters/test_mycomplexfnc.npy`. Then, the next time I run `py.test`, the output of the `mycomplexfnc()` will be compared to 4 digits against the old saved version.

Modifying this to work with pandas dataframes or other objects would be relatively simple. It could also be refactored to work with general objects without much effort, but, in my case, all the functions where I don't have anything better than a golden master test are functions that return arrays.

Should you put the saved golden master test results in version control? I would say yes, since they are necessary for properly testing the code base. 

## Slow tests

Sometimes I have tests that take a little while to run and I don't want them to run every single time I run `py.test`. So, I add an opt-in option for running slow tests, following the directions [on the py.test docs](https://docs.pytest.org/en/latest/example/simple.html#control-skipping-of-tests-according-to-command-line-option).

## pdb + ipdb
I thought I'd just add a note about debuggers, since I'm way more productive with a debugger at hand. When my tests fail and I can't figure out why, the first step is to use a debugger to really understand the code. The (P)ython (D)e(b)ugger. Also, the (IP)ython (D)e(b)ugger. These are super handy for dropping into some code to check values/step through the code/general debugging! It combines some of the playfulness of jupyter notebooks with python modules.

Just add these two lines:

```
import ipdb
ipdb.set_trace()
```

or 

```
import pdb
pdb.set_trace()
```

And then when those lines are run, execution will stop and I'm dropped into a debugging prompt where I can step through the code, examine variable values and other nice things.
