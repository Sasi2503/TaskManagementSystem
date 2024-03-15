class TaskViewModel:
    def __init__(self,taskID, Assignedby, Title, Description,  DueDate, Status, Priority):
        self.taskID = taskID
        self.Assignedby = Assignedby
        self.Title = Title
        self.Description=Description,  
        self.DueDate = DueDate
        self.Status = Status
        self.Priority = Priority


# def __init__(self,AssignedID, TaskID, AssignedTo,  DueDate, Status, PriorityID):
#         self.AssignedID = AssignedID
#         self.TaskID = TaskID
#         self.AssignedTo = AssignedTo
#         self.PriorityID = PriorityID
#         self.Status = Status
#         self.DueDate = DueDate