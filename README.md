# Expense Tracker Application Design Document

**Group 5 – MSCS632: Advanced Programming Languages**  
**Designed by:** Dheeraj Kollapaneni  
**Date:** May 25, 2025

---

## 1. Project Overview

The Expense Tracker Application is a CLI-based tool built in both **Python** and **C++** that enables users to add, view, filter, and summarize their expenses. This dual-language development approach is designed to illustrate key differences in programming language design such as **data types, memory management, naming, and binding**. This application also serves as a comparative study between the simplicity of Python’s high-level abstractions and C++’s performance-driven, statically typed structures.

---

![CleanShot 2025-05-25 at 21 57 31@2x](https://github.com/user-attachments/assets/a979448c-2bd7-481f-8af8-63e956927eaa)



## 2. Functional Requirements

- **Add Expense**: Includes date, amount, category, and description  
- **View All Expenses**  
- **Filter/Search Expenses**: By Date Range and/or Category  
- **Summarize Expenses**: By Category and Total Amount  
- **Unit Testing**: For Core Features (Python only)

---

## 3. Architecture and Components

| **Component**        | **Python Implementation**                  | **C++ Implementation**                   |
|----------------------|--------------------------------------------|------------------------------------------|
| Data Storage         | List of dictionaries                       | Vector of structs                         |
| Expense Entry        | Dict keys: date, amount, category, desc    | Struct fields: date, amount, category, desc |
| Filtering            | List comprehensions                        | For-loops with conditionals              |
| Summarization        | Dict-based aggregation                    | Map for category totals                  |
| Date Handling        | `datetime.strptime()`                      | Manual or `ctime` parsing                |
| Persistence (optional) | JSON file                                | `fstream` or CSV output                  |

---

## 4. User Interface Design (CLI)

Users interact through a command-line interface with menu-driven prompts:

1. Add Expense  
2. View Expenses  
3. Filter by Date or Category  
4. Show Summary  
5. Exit  

Each option will call relevant functions to process user input and display results.

---

## 5. Python Design Considerations

- High-level and dynamically typed  
- Uses built-in `list`, `dict`, and `datetime` modules  
- Supports JSON I/O for persistence  
- Unit tests created using standard `unittest` module  

---

## 6. C++ Design Considerations

- Uses `structs` for static typing and strong memory control  
- STL containers such as `vector`, `map`, and `string`  
- File I/O handled with `fstream`  
- Date handled manually or with `std::chrono` if needed  

---

## 7. Anticipated Challenges and Mitigation Strategies

- **Python**: Date parsing and lack of static type safety – mitigated via input validation.  
- **C++**: Verbose syntax and memory control issues – mitigated by STL use and scoped constructs.  
- **Testing**: Python includes unit tests; C++ will require manual validation or use of assertions.  

---

## 8. Timeline and Task Assignments

| **Task**               | **Deadline** | **Assigned To**            |
|------------------------|--------------|-----------------------------|
| Design Finalization    | May 25       | Dheeraj Kollapaneni         |
| Python Implementation  | May 28       | Bhargava B. Bharadwaj       |
| C++ Implementation     | May 28       | Aman Shah                   |
| Documentation          | May 30       | Nischal Pokharel            |
| Presentation           | May 30       | Suvendu Bista               |
| Final Review & Submission | May 31    | Entire Team                 |
