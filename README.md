# Structured Data Manager (CLI)

## Overview

Structured Data Manager is a command-line application that allows users to manage structured data using basic operations like create, read, update, and delete (CRUD).

The system stores data in memory using Python data structures and provides an interface to interact with it through a CLI.

---

## Features

* Add new records
* View all records
* Update existing records
* Delete records
* Simple and interactive CLI menu

---

## How It Works

### Data Storage

* Data is stored in memory using a list or dictionary
* Each record is structured (e.g., key-value pairs)

### Operations

* **Create** → Add new structured data
* **Read** → Display stored data
* **Update** → Modify existing data
* **Delete** → Remove data

---

## Project Structure

```
project/
│
├── main.py          # Handles CLI interaction (input/output)
├── operations.py    # Core logic (CRUD operations)
├── helpers.py       # Utility functions (validation, formatting)
└── README.md        # Project documentation
```

---

## Example Flow

1. User selects an option from CLI
2. Input is taken
3. Operation is performed
4. Result is displayed

---

## Learning Outcomes

* Understanding of CRUD operations
* Basic data structures (list, dict)
* Separation of concerns (input vs logic vs helpers)
* Building interactive CLI applications

---

## Limitations

* Data is not persistent (lost after program stops)
* No file/database storage
* Basic validation only

---

## Future Improvements

* Add file storage (Project 3)
* Improve validation and error handling
* Add search and filtering features

---
