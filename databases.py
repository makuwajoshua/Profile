# Importing libraries.
import sqlite3
import json
import xml.etree.ElementTree as ET

# Establish a connection to the SQLite database.
try:
    conn = sqlite3.connect("HyperionDev.db")
except sqlite3.Error:
    # Error handling if the database connection fails
    print("Please store your database as HyperionDev.db")
    quit()

# Create a cursor object to interact with the database.
cur = conn.cursor()

def usage_is_incorrect(input, num_args):
    """
    Checks if the command input has the correct number of arguments.

    Parameters:
        input (list): The command input list where the first element is the name.
        num_args (int): The expected number of arguments for the command.

    Returns:
         boolean: True if the number of arguments is incorrect and False otherwise.
    
    """
    if len(input) != num_args + 1:
        print(f"The {input[0]} command requires {num_args} arguments.")
        return True
    return False

def store_data_as_json(data, filename):
    """
    Stores data as a JSON file.

    Parameters:
        data (dict or list): The data to be stored in JSON format.
        filename (str): The name of the Json file to save the data.

    Returns:
        None.
    
    """
    try:
        # Writes the data to a JSON file.
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, sort_keys=True, indent=4)

        print(f"Data successfully saved to {filename} in UTF-8 encoding.")
   
    except Exception as e:
        # Handle any exceptions that might occur during file writing.
        print(f"Error occurred while saving the file: {e}")

def store_data_as_xml(data, filename):
    """
    Stores data as an XML file.

    Parameters:
        data (list): A list of dictionaries containing data to store in XML format.
        filename (str): The name of the XML file to save the data.

    Returns:
        None
    
    """
    try:
        # Create the root element of the XML.
        root = ET.Element("root")

        # Loops through each item in the data list.
        for item in data:

            # Create an entry element for each item.
            entry = ET.SubElement(root, "entry")

            # Loop through each key-vale pair in the item dictionary.
            for key, value in item.items():

                # Create a child element for each key with its value as text.
                child = ET.SubElement(entry, key)
                child.text = str(value)

        # Create an ElementTree object.
        tree = ET.ElementTree(root)

        # Writes the ElemenTree to a file.
        with open(filename, "wb") as file:
            tree.write(file, encoding="utf-8", xml_declaration=True)
        print(f"Data successfully saved to {filename} in UTF-8 encoding.")
    
    # Handles any exception that may occur during the writing process.
    except Exception as e:
        print(f"Error occurred while saving the file: {e}")

def offer_to_store(data):
    """
    Offers the user an option to store data as JSON or XML.

    Parameters:
        data (list or dict): The data to be stored.

    Returns:
        None
    
    """
    while True:
        # Prompt the user to choose whether to save the data.
        choice = input("Would you like to store this result? Y/[N]: ").strip().lower()
        
        if choice == "y":

            # Ask the user to specify the filename with either .xml or .json extension
            filename = input("Specify filename. Must end in .xml or .json: ")
            ext = filename.split(".")[-1]

            if ext == 'xml':
                store_data_as_xml(data, filename)
            elif ext == 'json':
                store_data_as_json(data, filename)
            else:
                print("Invalid file extension. Please use .xml or .json.")
            break
        
        # Exit the loop if the user chooses not to save.
        elif choice == 'n':
            break
        
        # Inform the user if they entered an invaid choice.
        else:
            print("Invalid choice.")

usage = '''
What would you like to do?

d - demo
vs <student_id>            - view subjects taken by a student
la <firstname> <surname>   - lookup address for a given firstname and surname
lr <student_id>            - list reviews for a given student_id
lc <teacher_id>            - list all courses taken by teacher_id
lnc                        - list all students who haven't completed their course
lf                         - list all students who have completed their course and achieved 30 or below
e                          - exit this program

Type your option here: '''

print("Welcome to the data querying app!")

while True:
    print()

    # Spilts the input data into a list.
    user_input = input(usage).split(" ")

    print()

    command = user_input[0]
    args = user_input[1:] if len(user_input) > 1 else []

    # demo - prints all student names and surnames.
    if command == 'd':
        
        # Extracts data from the database.
        data = cur.execute("SELECT * FROM Student").fetchall()

        # Models the output data as a list of dictionaries.
        results = [{"firstname": firstname, "surname": surname} for _, firstname, surname, _, _ in data]
        for result in results:
            print(f"{result['firstname']} {result['surname']}")

        # Calls the function that offers to save or not save the data in xml or json format.
        offer_to_store(results)

    # view subjects by student_id.
    elif command == 'vs':
        if usage_is_incorrect(user_input, 1):
            continue
        student_id = args[0]

        # Extracts data from the database.
        data = cur.execute('''
            SELECT Course.course_name, Course.course_code
            FROM StudentCourse 
            INNER JOIN Course ON StudentCourse.course_code = Course.course_code
            WHERE StudentCourse.student_id = ?
        ''', (student_id,)).fetchall()
        
        # Models the output data as a list of dictionaries.
        results = [{"course_name": course_name, "course_code": course_code} for course_name, course_code in data]
        
        # Iterates through the list of dictionary and prints the results.
        for result in results:
            print(f"{result['course_name']} ({result['course_code']})")

        # Calls the function that offers to save or not save the data in xml or json format.
        offer_to_store(results)

    # list address by name and surname.
    elif command == 'la':
        if usage_is_incorrect(user_input, 2):
            continue
        firstname, surname = args

        # Extracts data from the database.
        data = cur.execute('''
            SELECT Address.street, Address.city
            FROM Student
            INNER JOIN Address ON Student.address_id = Address.address_id
            WHERE Student.first_name = ? AND Student.last_name = ?
        ''', (firstname, surname)).fetchall()
        
        # Models the output data as a list of dictionaries.
        results = [{"street": street, "city": city} for street, city in data]
        
        # Iterates through the list of dictionary and prints the results.
        for result in results:
            print(f"Street: {result['street']}, City: {result['city']}")

        # Calls the function that offers to save or not save the data in xml or json format.
        offer_to_store(results)

    # list reviews for a given student_id.
    elif command == 'lr':
        if usage_is_incorrect(user_input, 1):
            continue
        student_id = args[0]

        # Extracts data from the database.
        data = cur.execute('''
            SELECT Review.review_text, 
                   Review.completeness, 
                   Review.efficiency, 
                   Review.style, 
                   Review.documentation
            FROM Review
            WHERE student_id = ?
        ''', (student_id,)).fetchall()
        
        # Models the output data as a list of dictionaries.
        results = [
            {
                "review_text": review_text,
                "completeness": completeness,
                "efficiency": efficiency,
                "style": style,
                "documentation": documentation
            } for review_text, completeness, efficiency, style, documentation in data
        ]
        
        # Iterates through the list of dictionary and prints the results.
        for result in results:
            print(f"""
                  Review: {result['review_text']}
                  Completeness: {result['completeness']}
                  Efficiency: {result['efficiency']}
                  Style: {result['style']}
                  Documentation: {result['documentation']}
                  """)

        # Calls the function that offers to save or not save the data in xml or json format.
        offer_to_store(results)

    # list all courses taken by teacher_id.
    elif command == 'lc':
        if usage_is_incorrect(user_input, 1):
            continue
        teacher_id = args[0]

        # Extracts data from the database.
        data = cur.execute('''
            SELECT Course.course_name
            FROM Course
            WHERE teacher_id = ?
        ''', (teacher_id,)).fetchall()

        # Models the output data as a list of dictionaries.
        results = [{"course_name": course_name} for course_name, in data]
        
        # Iterates through the list of dictionary and prints the results.
        for result in results:
            print(f"Course Name: {result['course_name']}")

        # Calls the function that offers to save or not save the data in xml or json format.
        offer_to_store(results)
    
    # list all students who haven't completed their course.
    elif command == 'lnc':
        # Extracts data from the database.
        data = cur.execute('''
            SELECT Student.student_id,
                   Student.first_name,
                   Student.last_name,
                   Student.email,
                   Course.course_name
            FROM Student
            INNER JOIN StudentCourse ON Student.student_id = StudentCourse.student_id
            INNER JOIN Course ON StudentCourse.course_code = Course.course_code
            WHERE StudentCourse.is_complete = 0;
        ''').fetchall()

        # Models the output data as a list of dictionaries.
        results = [
            {
                "ID": student_id,
                "First Name": first_name,
                "Last Name": last_name,
                "Email": email,
                "Course Name": course_name
            }
            for student_id, first_name, last_name, email, course_name in data
        ]
        
        # Iterates through the list of dictionary and prints the results.
        for result in results:
            print(f"""
                  ID: {result['ID']}
                  First Name: {result['First Name']}
                  Last Name: {result['Last Name']}
                  Email: {result['Email']}
                  Course Name: {result['Course Name']}
                  """)

        # Calls the function that offers to save or not save the data in xml or json format.
        offer_to_store(results)

    # list all students who have completed their course and got a mark <= 30.
    elif command == 'lf':
        # Extracts data from the database.
        data = cur.execute('''
            SELECT Student.student_id,
                   Student.first_name,
                   Student.last_name,
                   Student.email,
                   Course.course_name,
                   StudentCourse.mark
            FROM Student
            INNER JOIN StudentCourse ON Student.student_id = StudentCourse.student_id
            INNER JOIN Course ON StudentCourse.course_code = Course.course_code
            WHERE StudentCourse.is_complete = 1 AND StudentCourse.mark <= 30
        ''').fetchall()

        # Models the output data as a list of dictionaries.
        results = [
            {
                "ID": student_id,
                "First Name": first_name,
                "Last Name": last_name,
                "Email": email,
                "Course Name": course_name,
                "Mark": mark
            }
            for student_id, first_name, last_name, email, course_name, mark in data
        ]

        # Iterates through the list of dictionary and prints the results.
        for result in results:
            print(f"""
                  ID: {result['ID']}
                  First Name: {result['First Name']}
                  Last Name: {result['Last Name']}
                  Email: {result['Email']}
                  Course Name: {result['Course Name']}
                  Mark: {result['Mark']}
                  """)

        # Calls the function that offers to save or not save the data in xml or json format.
        offer_to_store(results)

    # exit the program.
    elif command == 'e':
        print("Exiting program.")
        break

    else:
        print("Invalid command. Please try again.")

# Closes the database connection
conn.close()


