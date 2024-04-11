from abc import ABC, abstractmethod

class Component(ABC):
    """The Component interface sets the common method for all components."""

    @abstractmethod
    def is_completed(self):
        """Checks if the task is completed."""
        pass

    @abstractmethod
    def complete(self):
        """Marks the task as completed."""
        pass

    @abstractmethod
    def undo_completion(self):
        """Marks the task as not completed."""
        pass

    @abstractmethod
    def add(self, task):
        """Method to add a task (only for Composite)."""
        pass

    @abstractmethod
    def remove(self, task):
        """Method to remove a task (only for Composite)."""
        pass
