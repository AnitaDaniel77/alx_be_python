def daily_reminder(task, priority, time_bound):

if priority not in ["high", "medium", "low"]:
return "Invalid priority level."

if priority == "high":
    if time_bound == "yes":
       return f"Reminder:'{task}' is a high priority task that requires immediate attention today!"

else: 
     return f"Reminder: '{task}' is a high priority task. Youshould complete it as soon as possible."
   elif priority == "medium":
       if time_bound == "yes":
       return f"Reminder: '{task}' is a medium priority task that requires attention today."
      
else: 

     return f"Reminder: '{task}' is a medium priority task. Focus on it when possible." 
else: 
      if time_bound == "yes":
          return f"Reminder: '{task}' is a low priority task. You can complete it later today."
else: 
       return f"Note: '{task}' is a low priority task. Consider completing it when you have free time."

