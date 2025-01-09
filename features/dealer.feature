Feature: To-Do List Management
  As a user, I want to manage my to-do list so that I can keep track of my tasks.

  Scenario: Add a task to the to-do list
    Given an empty to-do list
    When I add a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: Remove a task from the to-do list
    Given a to-do list with the task "Buy groceries"
    When I remove the task "Buy groceries"
    Then the to-do list should be empty

  Scenario: Add multiple tasks to the to-do list
    Given an empty to-do list
    When I add the tasks "Buy groceries", "Clean the house", "Pay bills"
    Then the to-do list should contain "Buy groceries", "Clean the house", "Pay bills"

  Scenario: Remove a task that does not exist
    Given an empty to-do list
    When I try to remove the task "Non-existent task"
    Then an error should be raised with the message "Task not found"

  Scenario: Clear all tasks from the to-do list
    Given a to-do list with the tasks "Buy groceries", "Clean the house"
    When I clear the to-do list
    Then the to-do list should be empty

  Scenario: Add an empty task to the to-do list
    Given an empty to-do list
    When I try to add an empty task
    Then an error should be raised with the message "Task cannot be empty"
