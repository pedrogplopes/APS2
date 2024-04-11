from component_interface import Component

class Composite(Component):
    """Composite acts as a container that can hold both SimpleTask and other Composite instances."""

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def is_completed(self):
        """Checks if all subtasks are completed."""
        for task in self.tasks:
            if not task.is_completed():
                return False
        return True

    def complete(self):
        """Marks all subtasks as completed."""
        for task in self.tasks:
            task.complete()

    def undo_completion(self):
        """Marks all subtasks as not completed."""
        for task in self.tasks:
            task.undo_completion()

    def add(self, task):
        """Method to add a task."""
        self.tasks.append(task)

    def remove(self, task):
        """Method to remove a task."""
        self.tasks.remove(task)
