from component_interface import Component

class Leaf(Component):
    """Leaf represents individual tasks that don’t contain other elements."""

    def __init__(self, name):
        self.name = name
        self.completed = False

    def is_completed(self):
        """Checks if the task is completed."""
        return self.completed

    def complete(self):
        """Marks the task as completed."""
        self.completed = True

    def undo_completion(self):
        """Marks the task as not completed."""
        self.completed = False

    def add(self, task):
        """Method to add a task (only for Composite)."""
        print("Cannot add task to a simple task.")

    def remove(self, task):
        """Method to remove a task (only for Composite)."""
        print("Cannot remove task from a simple task.")
