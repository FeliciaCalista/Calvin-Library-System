# Calvin Library System

**Library Web** is a desktop-based library management system developed using **Python** with a graphical user interface (GUI) built in **Tkinter**. It allows users and staff to manage book collections, handle user interactions, borrow/return books, and monitor the library’s operation—all through a simple and interactive interface.

![Main Screenshot](MAIN.png)

---

## Features

- **Authentication System**
  - Login and Sign-Up simulation (via `Login.py` and `Sign_Up_Email.py`)
  - Staff and general user separation (`Home_Staff.py`, `Home.py`)

- **Book Management**
  - Add, update, and delete book entries
  - View book information and images
  - Genre and nationality tagging
  - Book cover images for visual display

- **Borrowing and Returning**
  - Borrow books (`Borrow.py`)
  - Return process (`Return.py`)
  - Tracks user activity via `history.csv`

- **Data Management**
  - Backend operations use CSV files (`book.csv`, `user.csv`, `staff.csv`, etc.)
  - Database utility modules (`DatabaseManager.py`, `DatabaseExecution.py`)

- **User Interface**
  - Custom UI backgrounds and styling (`ImageBackground.py`, `Header.py`)
  - Toplevel windows for dynamic content display
  - Organized navigation via `Menu.py` and `MainFrame.py`

---

## Technologies Used

- **Python 3.x**
- **Tkinter** – GUI Framework
- **CSV** – Lightweight data storage
- **Pillow** – Image processing
- **OS / Sys** – File and path handling
- **Email (smtplib)** – For sign-up validation

---

## License

This project is licensed under the **MIT License** – you are free to use, modify, and distribute this project with attribution.

---

## Contributors

- [@FeliciaCalista](https://github.com/FeliciaCalista) 
- [@gracehutapea1208](https://github.com/gracehutapea1208) 
- **Ema Nelvi Salensky** 

We worked together to build the full functionality and interface of the Calvin Library System.

---

## Contact
* Email: fckfelicia04@gmail.com
