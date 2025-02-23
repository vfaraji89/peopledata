# peopledata
People Data Handbook
# People Data Engineering

Welcome to my GitHub profile focused on People Data and Analytics! I specialize in building scalable data structures and functions for managing and analyzing people/HR data.

## 🔍 Core Expertise

- People Data Modeling & Architecture
- HR Analytics Functions & Pipelines 
- Employee Data Processing & ETL
- Workforce Analytics
- People Analytics Automation

## 📊 Data Structures for People Data

```python
class EmployeeRecord:
    def __init__(self):
        self.personal_info = {
            'employee_id': str,
            'name': str,
            'email': str,
            'department': str,
            'title': str,
            'hire_date': datetime,
            'manager_id': str
        }
        
        self.compensation = {
            'salary': float,
            'bonus': float,
            'equity': float,
            'currency': str
        }
        
        self.performance = {
            'ratings': list,
            'reviews': list,
            'goals': list
        }
