# 🧪 Testing

## PyTest

## Coverage

## Nox

[Nox] is a very useful tool for running any array of tests across differnt Python enviroments.

Include in our project `noxfile.py` is a basic script to run all your pytest tests against the most modern versions of Python. If you want to modify what versions it runs against you will find the list below in the file and simply tack it on to the list.

```
python_versions = ["3.10", "3.11", "3.12", "3.13"]
```

To run all your [Nox] scripts at once use the command:

```
task nox
```

Visit the [Nox Config](https://nox.thea.codes/en/stable/config.html) to see the full list of its capabilities.

[Nox]: (https://nox.thea.codes/en/stable/index.html)
