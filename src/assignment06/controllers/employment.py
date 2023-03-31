from models import employee as e

def get_employee_dict(csv):
    employee_dict = {}
    for employee_row in csv.values:
        employee_list = employee_row.strip().split(',')
        employee_id = int(employee_list[0].strip())
        name = employee_list[1].strip()
        address = employee_list[2].strip()
        ssn = employee_list[3].strip()
        date_of_birth = employee_list[4].strip()
        job_title = employee_list[5].strip()
        start_date = employee_list[6].strip()
        end_date = employee_list[7] .strip()
        employee = e.Employee(employee_id,name,address,ssn,date_of_birth,job_title,start_date,end_date)
        employee_dict[employee.employee_id] = employee
    return employee_dict

def get_employee_content(header, employee_dict):
    content = ''.join(header)
    if employee_dict:
        for e in employee_dict.values():
            content = f"{content}{e.employee_id},{e.name},{e.address},{e.ssn}," \
            f"{e.date_of_birth},{e.job_title},{e.start_date},{e.end_date}\n"
    return content.rstrip()

def get_employee_max_id(employee_dict):
    if employee_dict:
        employee_id = max(list(employee_dict.keys())) + 1
    else:
        employee_id = 1
    return employee_id
