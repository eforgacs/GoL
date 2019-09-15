from behave import *

from life import Life


@given(u'a 3x3 board')
def step_impl(context):
    # TODO: use a list comprehension to create this list.
    context.board = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]
    print(context.board)


@given(u'cell 1,1 is alive')
def step_impl(context):
    context.board[1][1] = 1
    print(context.board)


@given(u'life board instantiated')
def step_impl(context):
    context.life = Life(context.board)


@when(u'cycled')
def step_impl(context):
    context.life.update()


@when(u'board retrieved')
def step_impl(context):
    context.board = context.life.get_board()
    print(context.board)


@then(u'cell 1,1 is dead')
def step_impl(context):
    context.board[1][1] = 0
