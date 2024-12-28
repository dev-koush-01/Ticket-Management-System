# Ticket Management System

This project is a **Ticket Management System** built with **Flask** and **Bootstrap**. It allows users to manage event tickets by adding ticket numbers, marking entries, filtering tickets by status, and deleting records. The system is designed to be simple and efficient, utilizing a SQLite database for data persistence.

## Features

1. **Add Tickets**:
   - Users can add a new ticket by entering the ticket number.
   
2. **Mark Entry**:
   - Tickets can be marked as "Entered," and the entry time will be recorded.

3. **Filter Tickets**:
   - Tickets can be filtered by:
     - All
     - Entered
     - Not Entered

4. **Search Tickets**:
   - Search for tickets by ticket number.

5. **Delete Tickets**:
   - Remove a ticket from the system.

6. **Reset All Tickets**:
   - Reset all tickets to the "Not Entered" status and clear entry times.

7. **Responsive Design**:
   - Built with Bootstrap 5 for mobile-friendly layouts.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: SQLite
- **Timezone**: Asia/Kolkata

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/ticket-management-system.git
   cd ticket-management-system
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate # For Linux/Mac
   venv\Scripts\activate   # For Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

5. **Access the Application**:
   Open a web browser and go to `http://127.0.0.1:3000`.

## File Structure

```
project/
|-- app.py          # Main application script
|-- templates/
|   `-- index.html  # HTML template
|-- static/
|   |-- images/     # QR codes and social icons
|-- todo.db         # SQLite database file (auto-created on first run)
```

## Key Functionalities

### Routes

1. `/` (GET, POST):
   - Displays all tickets, supports search and filtering.
   - Handles ticket creation.

2. `/delete/<int:sno>`:
   - Deletes a ticket by its serial number (sno).

3. `/enter/<int:sno>`:
   - Marks a ticket as "Entered" and logs the entry time.

4. `/reset`:
   - Resets all tickets to "Not Entered."

### Models

- `ToDo`:
  - `sno`: Serial number (Primary Key)
  - `ticketNo`: Ticket number
  - `status`: Status of the ticket (default: "Not Entered")
  - `entry_time`: DateTime of entry

### Templates

- **Navbar**: Allows ticket search, addition, and status reset.
- **Table**: Displays tickets with actions for each ticket (Enter/Delete).
- **Footer**: Links to social media and contact information.

## Future Enhancements

1. User authentication for added security.
2. Exporting ticket data to CSV or Excel.
3. Adding support for multiple events.

## Author

Developed by **Koushik Chandra**

- GitHub: [dev-koush-01](https://github.com/dev-koush-01)
- LinkedIn: [Koushik Chandra](https://www.linkedin.com/in/koushik-chandra-b97989291/)
- Instagram: [@daskel.x](https://www.instagram.com/daskel.x/profilecard/?igsh=bXpnZ2xrMnA5MTB6)

## License

This project is licensed under the Apache License 2.0. See the LICENSE file for more details.

---

Enjoy managing your tickets efficiently with this system! 🚀


