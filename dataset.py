import random
from faker import Faker
import datetime
import pandas as pd
from datetime import datetime, timedelta
# Initialize Faker instance
fake = Faker('yo_NG')

# Function to generate random student data

def generate_student_data(num_records):
    students = []
    
    for i in range(1, num_records + 1):
        # Create a biased distribution: more chances for 1-8, fewer for 9
        activity_choices = [None] * 10 + [1, 2, 3] * 12 + [4] * 7  # 20% NULL, fewer 9's
        media_choice = ['Yes'] * 60 + ['No'] * 40 
        student = {
            'StudentID': i,
            'FirstName': fake.first_name(),
            'MiddleName': fake.first_name(),
            'Surname': fake.last_name(),
            'DateOfBirth': fake.date_of_birth(minimum_age=15, maximum_age=20),
            'Gender': random.choice(['Male', 'Female']),
            'EnrolmentDate': fake.date_between(start_date='-4y', end_date='today'),
            'DepartmentID': random.randint(1, 4),
            'Address': fake.address().replace('\n', ', '),
            'EmailAddress': fake.email(),
            'PhoneNumber': fake.phone_number(),
            'GuardianID': random.randint(1, 50),
            'ClassID': random.randint(1, 3),
            'SocialMedia_Access': random.choice(media_choice),
            'ActivityID': random.choice(activity_choices)  # Use biased choices
        }

        # Ensure 'ActivityID' is None or an integer, not a float
        if student['ActivityID'] is not None:
            student['ActivityID'] = int(student['ActivityID'])

        students.append(student)
    
    return students

# Generate 50 student records
student_data = generate_student_data(500)

# Example output of the first 5 records
student_df = pd.DataFrame(student_data)
student_df.to_csv('students.csv', index=False)
print(student_df.head())


# Function to generate random guardian data
def generate_guardian_data(num_records):
    guardians = []
    
    for i in range(1, num_records + 1):
        guardian = {
            'GuardianID': i,
            'GivenName': fake.first_name(),
            'Surname': fake.last_name(),
            'EmailAddress': fake.email(),
            'PhoneNumber': fake.phone_number()
        }
        guardians.append(guardian)
    
    return guardians

# Generate 50 guardians
guardian_data = generate_guardian_data(100)
guardian_df = pd.DataFrame(guardian_data)
guardian_df.to_csv('guardian.csv', index= False)
# Print or export the data
#print(guardian_df.head())

# Function to generate random teacher data
def generate_teacher_data(num_records):
    teachers = []
    
    for i in range(1, num_records + 1):
        teacher = {
            'TeacherID': i,
            'FirstName': fake.first_name(),
            'Surname': fake.last_name(),
            'EmailAddress': fake.unique.email(),
            'PhoneNumber': fake.phone_number(),
            'Address': fake.address().replace('\n', ', '),
            'Gender': random.choice(['M', 'F'])
        }
        teachers.append(teacher)
    
    return teachers

# Generate 50 teachers
teacher_data = generate_teacher_data(15)
teacher_df = pd.DataFrame(teacher_data)
teacher_df.to_csv('teacher.csv', index= False)
# Print or export the data
#print(teacher_df.head())


# generating class table
# List of allowed months excluding August, December, and April
allowed_months = ['January', 'February', 'March', 'May', 'June', 'July', 'September', 'October', 'November']

# Helper function to generate valid start and end dates
def generate_date_range():
    start_month = random.choice(allowed_months)
    start_year = random.randint(2020, 2024)
    start_date = f"10 {start_month} {start_year}"

    # Add 3 months to the start date to generate the end date
    # Exclude months: August, December, April
    month_index = allowed_months.index(start_month)
    end_month_index = (month_index + 3) % len(allowed_months)
    end_month = allowed_months[end_month_index]

    # Ensure correct year rollover if the end month is earlier in the year
    end_year = start_year if end_month_index > month_index else start_year + 1
    end_date = f"5 {end_month} {end_year}"

    return start_date, end_date


# Function to generate random class data with date ranges
def generate_class_data(num_records):
    classes = []
    
    for i in range(1, num_records + 1):
        # Map ClassID to the class name
        class_id = random.randint(1, 3)
        class_name = {1: 'SSS1', 2: 'SSS2', 3: 'SSS3'}[class_id]
        start_date, end_date = generate_date_range()
        class_entry = {
            'ClassID': class_id,
            'ClassName': class_name,
            'SubjectID': random.randint(1, 20),  # Assuming you have 20 subjects
            'TeacherID': random.randint(1, 15),  # Assuming you have 50 teachers
            'Year': random.randint(2020, 2024),  # Last few years of data
            'Term': random.choice(['First', 'Second', 'Third']),
            'StartDate': start_date,
            'EndDate': end_date
        }
        classes.append(class_entry)
    
    return classes

# Generate 50 classes
class_data = generate_class_data(50)
class_df = pd.DataFrame(class_data)
class_df.to_csv('class.csv', index= False)
# Print or export the data
#print(class_df.head())


# generating the department table
# Define department names and descriptions as a dictionary
department_data = {
    1: {'DepartmentName': 'Science', 'Description': 'The Science department offers courses in biology, chemistry, and physics.'},
    2: {'DepartmentName': 'Arts', 'Description': 'The Arts department covers literature, visual arts, and performing arts.'},
    3: {'DepartmentName': 'Commercial', 'Description': 'The Commercial department focuses on business studies and economics.'},
    4: {'DepartmentName': 'Engineering', 'Description': 'The Engineering department includes civil, mechanical, and electrical engineering courses.'},
}

# Function to generate random department data
def generate_department_data(num_records):
    departments = []
    
    for i in range(1, num_records + 1):
        department_entry = {
            'DepartmentID': i,  # Start ID from 1
            'DepartmentName': department_data[i]['DepartmentName'],  # Get the department name
            'HeadOfDepartment': fake.name(),  # Generate a random name for HOD
            'Description': department_data[i]['Description']  # Get the specific description
        }
        departments.append(department_entry)
    
    return departments

# Generate 4 departments
department_data_list = generate_department_data(4)
dept_df = pd.DataFrame(department_data_list)
dept_df.to_csv('department.csv', index=False)

# Print the DataFrame for verification
#print(dept_df)



# generating subject table
# List of common subjects
subject_names = {
    1:'Mathematics', 2:'English Language', 3:'Biology', 4:'Chemistry', 5:'Physics',
    6:'Geography', 7:'Government', 8:'Economics', 9:'Literature in English', 
    10:'Agricultural Science', 11:'Business Studies', 12:'Fine Arts', 
    13:'Computer Studies', 14:'History', 15:'Music', 16:'Physical Education'}

# Function to generate random subject data
subject_names = {
    1:'Mathematics', 2:'English Language', 3:'Biology', 4:'Chemistry', 5:'Physics',
    6:'Geography', 7:'Government', 8:'Economics', 9:'Literature in English', 
    10:'Agricultural Science', 11:'Business Studies', 12:'Fine Arts', 
    13:'Computer Studies', 14:'History', 15:'Music', 16:'Physical Education'}

# Function to generate random subject data
def generate_subject_data(num_records):
    subjects = []
    
    for i in range(1, num_records + 1):
        subject_entry = {
            'SubjectID': i,  # Use a sequential ID for subjects
            'SubjectName': subject_names[i]  # Get the subject name using the ID
        }
        subjects.append(subject_entry)
    
    return subjects


# Generate 16 subjects
subject_data = generate_subject_data(16)
subject_df = pd.DataFrame(subject_data)
subject_df.to_csv('subject.csv', index= False)

# Print or export the data
#print(subject_df.head())

# creating curricular activity table

# Define common extracurricular activities
activity_names = {
    1: 'Sports club',
    2: 'Social club',
    3: 'Religious Club',
    4: 'Extra lessons club'
}

# Function to generate random extracurricular activity data
def generate_extracurricular_activity_data(num_records):
    extracurricular_activities = []
    
    for i in range(1, num_records + 1):
        activity_entry = {
            'ActivityID': i,  # Sequential ID for each activity
            'ActivityName': activity_names[i],  # Use predefined activity name
            'Description': f"The {activity_names[i]} engages students in various creative and skill-building activities."  # Generic description
        }
        extracurricular_activities.append(activity_entry)
    
    return extracurricular_activities

# Generate extracurricular activities based on the predefined list
extracurricular_data = generate_extracurricular_activity_data(len(activity_names))
extracurricular_df = pd.DataFrame(extracurricular_data)
extracurricular_df.to_csv('extracurricular_activity.csv', index=False)

# Print the DataFrame for verification
#print(extracurricular_df.head())


# generating dataset for attendance

# Function to generate random attendance data
def generate_attendance_data(num_records, student_ids, class_ids):
    attendance_records = []
    
    for i in range(1, num_records + 1):
        attendance_entry = {
            'AttendanceID': i,  # Sequential ID for each attendance record
            'StudentID': random.choice(student_ids),  # Randomly select a StudentID from the list
            'ClassID': random.choice(class_ids),      # Randomly select a ClassID from the list
            'Date': fake.date_between(start_date='-30d', end_date='today'),  # Random date in the last 30 days
            'Status': random.choice(['Present', 'Absent', 'Late']),  # Random status
            'Remarks': fake.sentence(nb_words=10)  # Generate a random remark
        }
        attendance_records.append(attendance_entry)
    
    return attendance_records

# mapping the student and class tables previously generated to in order to use the student and class id 
student_ids = student_df['StudentID'].tolist()  # Extracting StudentID from existing DataFrame
class_ids = class_df['ClassID'].tolist()        # Extracting ClassID from existing DataFrame
attendance_data = generate_attendance_data(400, student_ids, class_ids)  # Generate 100 records
attendance_df = pd.DataFrame(attendance_data)
attendance_df.to_csv('attendance.csv', index=False)

# Print the DataFrame for verification
#print(attendance_df.head())


#generating academic records table

# Function to generate random academic record data
def generate_academic_record_data(num_records, student_ids, class_ids):
    academic_records = []
    
    for i in range(1, num_records + 1):
        year = random.randint(2020, 2024)  # Random year between 2020 and 2024
        term = random.choice(['First', 'Second', 'Third'])  # Randomly select term
        position = random.randint(1, 30)  # Assuming a maximum of 30 students in a class
        total_score = round(random.uniform(0, 100), 2)  # Random score between 0 and 100
        
        academic_entry = {
            'RecordID': i,  # Sequential ID for each academic record
            'Year': year, 
            'Term': term, 
            'Position': position,
            'TotalScore': total_score,
            'StudentID': random.choice(student_ids),  # Randomly select a StudentID
            'ClassID': random.choice(class_ids)       # Randomly select a ClassID
        }
        academic_records.append(academic_entry)
    
    return academic_records

# Assuming you already have student_df and class_df DataFrames
student_ids = student_df['StudentID'].tolist()  # Extracting StudentID from existing DataFrame
class_ids = class_df['ClassID'].tolist()        # Extracting ClassID from existing DataFrame

# Generate academic records
academic_data = generate_academic_record_data(400, student_ids, class_ids)  # Generate 400 records
academic_df = pd.DataFrame(academic_data)
academic_df.to_csv('academic_records.csv', index=False)

# Print the DataFrame for verification
#print(academic_df.head())



# Function to generate random subject performance data
def generate_subject_performance_data(num_records, student_ids, subject_ids, class_ids):
    subject_performances = []
    
    for i in range(1, num_records + 1):
        year = random.randint(2020, 2024)  # Random year between 2020 and 2024
        term = random.choice(['First', 'Second', 'Third'])  # Randomly select term
        score = round(random.uniform(0, 100), 2)  # Random score between 0 and 100
        
        performance_entry = {
            'PerformanceID': i,  # Sequential ID for each performance record
            'StudentID': random.choice(student_ids),  # Randomly select a StudentID
            'SubjectID': random.choice(subject_ids),  # Randomly select a SubjectID
            'ClassID': random.choice(class_ids),       # Randomly select a ClassID
            'Year': year, 
            'Term': term, 
            'Score': score
        }
        subject_performances.append(performance_entry)
    
    return subject_performances

# Sample data for student IDs, subject IDs, and class IDs (ensure you have these from your existing data)
student_ids = student_df['StudentID'].tolist()  # Extracting StudentID from existing DataFrame
subject_ids = subject_df['SubjectID'].tolist()  # Extracting SubjectID from existing DataFrame
class_ids = class_df['ClassID'].tolist()        # Extracting ClassID from existing DataFrame

# Generate subject performance records
subject_performance_data = generate_subject_performance_data(1000, student_ids, subject_ids, class_ids)  # Generate 400 records
subject_performance_df = pd.DataFrame(subject_performance_data)
subject_performance_df.to_csv('subject_performance.csv', index=False)

# Print the DataFrame for verification
#print(subject_performance_df.head())
