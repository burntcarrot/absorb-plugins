## Creating Plugins

`absorb` uses `click`, `click-plugins` and `setuptools` for creating and installing plugins.

The directory structure for our plugin `myext` would be as follows:

```
myext
│   setup.py
└───myext
        core.py
```

`setup.py` is the setup script for our plugin. It ensures that our plugin is installed appropriately in `absorb`.

Here are the contents of `setup.py`:

```python
from setuptools import setup

setup(
    name="myext",
    version="0.1.0",
    packages=["myext"],
    entry_points="""
        [absorb.plugins]
        myext=myext.core:mycommand
    """,
)
```

- The setuptools entry point `myext=myext.core:mycommand` in the above script is constructed in the form:
  - `<PLUGIN_NAME>=<PLUGIN_NAME>.<FILENAME>.<COMMAND_NAME>`
  - In our plugin, we have `myext` as the `<PLUGIN_NAME>`, and `core.py` as the `<FILENAME>` respectively.
  - Inside `core.py`, we have the `mycommand` command, which is to be registered as a part of our plugin. We can set `<COMMAND_NAME>` as `mycommand`.

`myext/core.py` is the core of our plugin.

Here are the contents of `core.py`:

```python
import click


@click.command()
@click.argument("name")
def mycommand(name):
    click.echo("Hi " + name + "!")
```

### Installation:

We can then install our plugins using `pip`:

```
pip install myext/
```

**(Slash is mandatory.)**

### Preview:

Here is a preview of our plugin:

![plugin](static/absorb-command.gif)
