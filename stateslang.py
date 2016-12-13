#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""States Language Python Definition"""
import attr
from jsonpath_rw import jsonpath, parse


def is_terminal(state):
    """Check if state is terminal."""
    return state.end or isinstance(state, (Succeed, Fail))


def next(state):
    """Get the next state."""
    if isinstance(state, Choice):
        return choose(state)
    else:
        return state.next


def choose(state):
    """Execute choice."""


@attr.s
class State(object):
    """Base state class"""
    type = attr.ib()
    comment = attr.ib(default="")


@attr.s
class Choice(State):
    """Choice state class"""
    choices = attr.ib(default=attr.Factory(list))


@attr.s
class ChoiceRule(object):
    """A choice rule"""
    name = attr.ib()


@attr.s
class AndChoiceRule(object):
    """An `and` choice rule"""


@attr.s
class OrChoiceRule(object):
    """An `and` choice rule"""
