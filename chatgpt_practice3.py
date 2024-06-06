# ChatGPT link: https://chatgpt.com/c/f5eb8a34-69a6-41d3-bc07-7a292f663e0f

class Task:
    def __init__(self, description, status, time_spent):
        self.description = description
        self.status = status
        self.time_spent = time_spent
    
    def __repr__(self):
        return f"Task: description = {self.description}, status = {self.status}, time_spent = {self.time_spent}"
    
    def update_status(self, new_status):
        self.status = new_status

    def update_time_spent(self, new_time):
        self.time_spent = new_time

class Employee:
    def __init__(self, employee_id):
        self.employee_id = employee_id
        self.tasks = {}
    
    def __repr__(self):
        tasks_repr = ', '.join([repr(task) for task in self.tasks.values()])
        return f"Employee: id = {self.employee_id}, tasks = [{tasks_repr}]"
    
    def __str__(self):
        tasks_str = ', '.join([str(task) for task in self.tasks.values()])
        return f"Employee ID: {self.employee_id}\nTasks:\n{tasks_str}"

    def add_task(self, description, status, time_spent):
        self.tasks[description] = Task(description, status, time_spent)
        print(f"New task added: '{description}'")

    def update_task_status(self, description, new_status):
        if description in self.tasks:
            self.tasks[description].update_status(new_status)
        else:
            print("Task not found.")

    def update_task_time(self, description, new_time):
        if description in self.tasks:
            self.tasks[description].update_time_spent(new_time)
        else:
            print("Task not found.")

class TaskManager:
    def __init__(self):
        self.employees = {}
    
    def __repr__(self):
        employees_repr = ', '.join([repr(employee) for employee in self.employees.values()])
        return f"TaskManager(employees=[{employees_repr}])"
    
    def __str__(self):
        employees_str = '\n'.join([str(employee) for employee in self.employees.values()])
        return f"TaskManager:\nEmployees:\n{employees_str}"
    
    def add_employee(self, employee_id):
        self.employees[employee_id] = Employee(employee_id)
        print(f"Employee ID '{employee_id}' was added.")

    def add_task(self, employee_id, description, status, time_spent):
        if employee_id in self.employees:
            self.employees[employee_id].add_task(description, status, time_spent)
            print(f"'{description}' added as task to employee ID '{employee_id}'")
        else:
            print(f"Employee with ID '{employee_id}' not found.")

    def update_task_status(self, employee_id, description, new_status):
        if employee_id in self.employees:
            self.employees[employee_id].update_task_status(description, new_status)
            print(f"'{description}' status updated to '{new_status}'")
        else:
            print(f"Employee with ID '{employee_id}' not found.")

    def update_task_time(self, employee_id, description, new_time):
        if employee_id in self.employees:
            self.employees[employee_id].update_task_time(description, new_time)
            print(f"'{description}' time spent updated to '{new_time}'")
        else:
            print(f"Employee with ID '{employee_id}' not found.")

    def print_employee_summary(self, employee_id):
        if employee_id in self.employees:
            print(self.employees[employee_id])
        else:
            print(f"Employee with ID '{employee_id}' not found.")

# Create a TaskManager instance
manager = TaskManager()

# Add employees
manager.add_employee('E001')
manager.add_employee('E002')

# Add tasks to employees
manager.add_task('E001', 'Complete report', 'in progress', 2)
manager.add_task('E001', 'Update website', 'completed', 5)
manager.add_task('E002', 'Prepare presentation', 'in progress', 3)

# Update task status
manager.update_task_status('E001', 'Complete report', 'completed')

# Update task time spent
manager.update_task_time('E001', 'Complete report', 3)

# Print summary for an employee
manager.print_employee_summary('E001')