# 👨‍💻 Data Querying App

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?logo=sqlite&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-Data-orange?logo=json&logoColor=white)
![XML](https://img.shields.io/badge/XML-Data-red?logo=xml&logoColor=white)

Welcome to the Data Querying App! This Python-based application provides an interface for querying a SQLite database, 
retrieving data, and storing results in JSON or XML formats.
The app is user-friendly and demonstrates core database operations.

---

## Features
- **Database Connection**: Seamless connection to an SQLite database.
- **Data Retrieval**: Query student and course-related information.
- **Data Export**: Save results in JSON or XML formats.
- **Interactive Interface**: User-friendly command-line menu.
- **Error Handling**: Robust error management for seamless execution.

---

## Prerequisites
- Python 3.x
- SQLite database file (`HyperionDev.db`)

Install the required dependencies:
```bash
pip install sqlite3
```

---

## Usage
Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/yourusername/data-querying-app.git
cd data-querying-app
```
Ensure the SQLite database file (`HyperionDev.db`) is stored in the project directory.

Run the application:
```bash
python app.py
```

### Command Menu
The application provides the following commands:
| Command           | Description |
|-------------------|-------------|
| `d`              | Demo: Displays all student names and surnames. |
| `vs <student_id>` | View subjects taken by a student. |
| `la <firstname> <surname>` | Lookup address for a given firstname and surname. |
| `lr <student_id>` | List reviews for a given student ID. |
| `lc <teacher_id>` | List all courses taught by a teacher. |
| `lnc`            | List all students who haven’t completed their course. |
| `lf`             | List students who completed their course with marks ≤30. |
| `e`              | Exit the program. |

---

## Screenshots
### Command Menu and Student database:
![image](https://github.com/user-attachments/assets/3d4d68ab-2063-4d6d-823c-365e47c1cfb7)
![image](https://github.com/user-attachments/assets/5800917a-09a5-43ea-976d-e95c79baef8d)


### Example JSON Query and Output:
![image](https://github.com/user-attachments/assets/009c7892-8075-43e9-a055-12dd2b50cb8a)
![image](https://github.com/user-attachments/assets/79ae1ed2-7acd-474b-aaf0-9b248fe43ca6)



### Example XML Query and Output:
![image](https://github.com/user-attachments/assets/074d5722-d11f-40a3-840f-9e55fdb739b6)
![image](https://github.com/user-attachments/assets/6f8be9f0-c3f5-4425-88ee-4d083670d082)


---

## 💻 Code Highlights
### Database Connection:
```python
conn = sqlite3.connect("HyperionDev.db")
cur = conn.cursor()
```

### Export to JSON:
```python
with open(filename, 'w', encoding='utf-8') as file:
    json.dump(data, file, sort_keys=True, indent=4)
```

### Export to XML:
```python
root = ET.Element("root")
for item in data:
    entry = ET.SubElement(root, "entry")
    for key, value in item.items():
        child = ET.SubElement(entry, key)
        child.text = str(value)
```
## Acknowledgments
Special thanks to the HyperionDev community and mentors for their continuous support.

- Python Community: For valuable resources and support.

--

![GitHub](https://img.shields.io/github/stars/yourusername/data-querying-app?style=social)

