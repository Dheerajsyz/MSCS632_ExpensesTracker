# Expense Tracker Application

**Developed by:** Suvendu Bista, Aman Shah, Dheeraj Kollapaneni, Nischal Pokhrel, Bhagavannarayana Bharadwaj Swayampakula

**Course:** MSCS632 - A01 Advanced Programming Languages
**Professor:** Vanessa Cooper
**Date:** May 25, 2025

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Functional Requirements](#functional-requirements)
3. [Architecture and Components](#architecture-and-components)
4. [Flowchart Diagram](#flowchart-diagram)
5. [Class Diagram](#class-diagram)

   * [Python](#python)
   * [C++](#c)
6. [User Interface Design (CLI)](#user-interface-design-cli)
7. [Design Considerations](#design-considerations)

   * [Python](#python-1)
   * [C++](#c-1)
8. [Collaboration Methodology](#collaboration-methodology)
9. [Anticipated Challenges and Mitigation Strategies](#anticipated-challenges-and-mitigation-strategies)
10. [Timeline and Task Assignments](#timeline-and-task-assignments)
11. [Repository Link](#repository-link)

---

## Project Overview

The **Expense Tracker Application** is a command-line interface (CLI) tool developed in both **Python** and **C++**. It enables users to:

* Add expenses (date, amount, category, description)
* View all recorded expenses
* Filter/search expenses by date range and/or category
* Summarize expenses by category and total amounts
* (Python only) Execute unit tests for core features

This dual-language implementation illustrates differences in language design, including data handling, memory management, and abstraction levels, providing a comparative study of Python’s high-level features versus C++’s performance-driven, statically-typed structures.

---

## Functional Requirements

* **Add Expense**: Capture date, amount, category, description.
* **View Expenses**: Display all saved expenses.
* **Filter/Search**: Filter by date range and/or category.
* **Summarize**: Aggregate totals by category and overall sum.
* **Unit Testing**: (Python only) Validate core functionalities via tests.

---

## Architecture and Components

| Component               | Python Implementation                                   | C++ Implementation                                                                                   |
| ----------------------- | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Data Storage            | List of dictionaries                                    | `std::vector` of structs                                                                             |
| Expense Entry Structure | Dict keys (`date`, `amount`, `category`, `description`) | `struct Expense { std::string date; double amount; std::string category; std::string description; }` |
| Filtering               | List comprehensions                                     | `for` loops with conditionals                                                                        |
| Summarization           | Dict-based aggregation                                  | `std::map` for category totals                                                                       |
| Date Handling           | `datetime.strptime()`                                   | Manual parsing or `std::chrono`                                                                      |
| Persistence (optional)  | JSON file via `json` module                             | File I/O with `std::fstream` or CSV                                                                  |

---

## Flowchart Diagram

![image](https://github.com/user-attachments/assets/7aecb425-c86a-473e-b75e-bd3d5d383bd5)


*Figure: Expense Tracker Application flowchart.*

---

## Class Diagram

### Python


![image](https://github.com/user-attachments/assets/706e603f-518f-4c32-a8c7-0c6bcb34a67d)


*Figure: Python class diagram illustrating data structures and module relationships.*

### C++

![image](https://github.com/user-attachments/assets/a8ff6079-2640-49c3-872f-e32f900eca1b)


*Figure: C++ class diagram showing structs and STL container usage.*

---

## User Interface Design (CLI)

Users interact through a menu-driven CLI:

```
1. Add Expense
2. View Expenses
3. Filter by Date or Category
4. Show Summary
5. Exit
```

Each selection invokes the corresponding function to process input and display results.

---

## Design Considerations

### Python

* High-level, dynamically typed language
* Utilizes built-in `list`, `dict`, and `datetime` modules
* JSON I/O for persistence
* Unit tests implemented with `unittest`

### C++

* Static typing with `struct` for expense entries
* Uses STL containers (`std::vector`, `std::map`, `std::string`)
* File I/O via `std::fstream`
* Manual date handling or `std::chrono`

---

## Collaboration Methodology

* **Version Control:** GitHub repository
* **Communication:** Microsoft Teams, Email

---

## Anticipated Challenges and Mitigation Strategies

* **Python**: Date parsing errors & lack of static type safety → Mitigated through input validation.
* **C++**: Verbose syntax & memory management → Mitigated via STL usage and scoped constructs.
* **Testing**: Python unit tests; C++ validation through assertions or manual testing.

---

## Timeline and Task Assignments

| Task                      | Deadline   | Assigned To           |
| ------------------------- | ---------- | --------------------- |
| Design Finalization       | 2025-05-25 | Dheeraj Kollapaneni   |
| Python Implementation     | 2025-06-08 | Bhargava B. Bharadwaj |
| C++ Implementation        | 2025-06-08 | Aman Shah             |
| Documentation             | 2025-06-22 | Nischal Pokhrel       |
| Presentation              | 2025-06-22 | Suvendu Bista         |
| Final Review & Submission | 2025-06-22 | Entire Team           |

---

## Repository Link

[View the GitHub Repository](https://github.com/Dheerajsyz/MSCS632_Group-Project)
