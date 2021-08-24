from pkg_resources import iter_entry_points

import click
from click_plugins import with_plugins


@with_plugins(iter_entry_points("zoo.plugins"))
@click.group()
def zoo():
    pass


@zoo.command()
def cat():
    print("🐱 meow!")


@zoo.command()
def dog():
    print("🐕 what da dog doin?")
