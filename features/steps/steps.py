from behave import given, when, then
from todo_app import ToDoList

@given('an empty to-do list')
def step_given_empty_todo_list(context):
    context.todo_list = ToDoList()

@given('a to-do list with the task "{task}"')
def step_given_todo_list_with_task(context, task):
    context.todo_list = ToDoList()
    context.todo_list.add_task(task)

@given('a to-do list with the tasks "{tasks}"')
def step_given_todo_list_with_tasks(context, tasks):
    context.todo_list = ToDoList()
    for task in tasks.split(", "):
        context.todo_list.add_task(task)

@when('I add a task "{task}"')
def step_when_add_task(context, task):
    context.todo_list.add_task(task)

@when('I add the tasks "{tasks}"')
def step_when_add_multiple_tasks(context, tasks):
    for task in tasks.split(", "):
        context.todo_list.add_task(task)

@when('I remove the task "{task}"')
def step_when_remove_task(context, task):
    context.todo_list.remove_task(task)

@when('I try to remove the task "{task}"')
def step_when_try_remove_nonexistent_task(context, task):
    try:
        context.todo_list.remove_task(task)
    except ValueError as e:
        context.error = str(e)

@when('I try to add an empty task')
def step_when_try_add_empty_task(context):
    try:
        context.todo_list.add_task("")
    except ValueError as e:
        context.error = str(e)

@when('I clear the to-do list')
def step_when_clear_todo_list(context):
    context.todo_list.clear_tasks()

@then('the to-do list should contain "{tasks}"')
def step_then_todo_list_contains(context, tasks):
    expected_tasks = tasks.split(", ")
    actual_tasks = context.todo_list.get_tasks()
    assert actual_tasks == expected_tasks, f"Expected {expected_tasks}, but got {actual_tasks}"

@then('the to-do list should be empty')
def step_then_todo_list_empty(context):
    assert len(context.todo_list.get_tasks()) == 0, "Expected the list to be empty"

@then('an error should be raised with the message "{message}"')
def step_then_error_raised_with_message(context, message):
    assert hasattr(context, "error"), "No error was raised"
    assert context.error == message, f"Expected error message '{message}', but got '{context.error}'"
