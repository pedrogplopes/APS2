from leaves import Leaf
from composite import Composite

def display_task_structure(task, indent=0):
    """Recursively display the task structure."""
    if isinstance(task, Leaf):
        completion_status = "Completed" if task.is_completed() else "Not Completed"
        print("  " * indent + f"Leaf: {task.name} - {completion_status}")
    elif isinstance(task, Composite):
        completion_status = "Completed" if task.is_completed() else "Not Completed"
        print("  " * indent + f"Composite: {task.name} - {completion_status}")
        for child in task.tasks:
            display_task_structure(child, indent + 1)

if __name__ == "__main__":
    task1 = Leaf("Leaf 1")
    task2 = Leaf("Leaf 2")
    task3 = Leaf("Leaf 3")
    task4 = Leaf("Leaf 4")
    task5 = Leaf("Leaf 5")
    task6 = Leaf("Leaf 6")
    task7 = Leaf("Leaf 7")
    task8 = Leaf("Leaf 8")
    task9 = Leaf("Leaf 9")
    task10 = Leaf("Leaf 10")
    task11 = Leaf("Leaf 11")
    task12 = Leaf("Leaf 12")

    composite1 = Composite("Composite 1")
    composite2 = Composite("Composite 2")
    composite3 = Composite("Composite 3")
    composite4 = Composite("Composite 4")

    # Composite 1
    composite1.add(task1)
    composite1.add(task2)
    composite1.add(task3)
    composite1.add(task4)

    # Composite 2
    composite2.add(composite1)
    composite2.add(task5)
    composite2.add(task6)
    composite2.add(task7)

    # Composite 3
    composite3.add(composite2)
    composite3.add(task8)
    composite3.add(task9)
    composite3.add(task10)

    # Composite 4
    composite4.add(composite3)
    composite4.add(task11)
    composite4.add(task12)

    
    task1.complete()
    task2.complete()
    task3.complete()
    task4.complete()
    task5.complete()
    task6.complete()
    task7.complete()
    task11.complete()
    task12.complete()

    print("Árvore de componentes:")
    display_task_structure(composite4)


