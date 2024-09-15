# Currency Converter

A simple web-based currency converter built with Django that allows users to convert between different currencies using real-time exchange rates. The app also tracks the conversion history.

## Features

- **Currency Conversion**: 
  - Users can input an amount and select two currencies (e.g., USD to EUR) to convert between.
  - The app fetches live exchange rates using the Open Exchange Rates API.
  
- **Real-time Exchange Rates**: 
  - Fetches live exchange rates from the [Open Exchange Rates API](https://openexchangerates.org/).
  
- **Conversion History**: 
  - The app tracks the user's last 10 conversions and displays the history.
  - Option to clear the conversion history.


## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (Flexbox for layout), Django templates
- **Database**: SQLite (for storing conversion history)
- **API**: Open Exchange Rates API for fetching real-time exchange rates

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.x**
- **Django 3.x** (or above)
- **pip** (Python package manager)

## App Screenshot
![image](https://github.com/user-attachments/assets/c7dba333-8184-44a2-97d8-51cec4971eaf)


## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/0kogu/Currency-Converter.git
   cd currency-converter
