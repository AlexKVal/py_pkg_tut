# Example Package

https://packaging.python.org/tutorials/packaging-projects/

Steps to build a [wheel](https://pythonwheels.com/) distribution
```
> pip install setuptools wheel
> python3 setup.py sdist bdist_wheel
```

Now publish it.
Register an account at https://test.pypi.org/account/register/
```
> pip install twine
> twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

Now install it (probably create a new [virtualenv](https://packaging.python.org/key_projects/#virtualenv))
```
> pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-your-username
```

Check that it works
```
> python
>>> from example_pkg import name, secret
>>> name
'example_pkg'
>>> secret
'blah blah'
```

Congratulations, you’ve packaged and distributed a Python project! ✨ 🍰 ✨

The result can be seen here https://test.pypi.org/project/example-pkg-alexkval/
