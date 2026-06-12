# Hotel Management System

A comprehensive hotel management system built with Python and Tkinter that provides a user-friendly graphical interface for managing room bookings, customer details, payments, and food services.

## Features

### 1. **Room Management**
- 6 pre-configured rooms with different types and capacities:
  - **AC Rooms**: Room 101, 102, 301
  - **Non-AC Rooms**: Room 201, 202, 302
- Room details include type, capacity, availability status, and daily rates
- Real-time availability tracking

### 2. **New Booking**
- Collect customer information:
  - Name
  - Phone Number
  - Address
  - Aadhar Number
- Select available rooms based on:
  - Room type (AC/Non-AC)
  - Capacity
  - Daily rate
- Specify number of days for stay

### 3. **Payment System**
- Calculate total room charges based on days and daily rate
- Multiple payment modes:
  - PhonePe
  - Card
  - Cash
- Track total number of bookings in the system

### 4. **Food Service**
- Two ordering options:
  - Order to Room
  - Book a Table
- Restaurant menu with 9 food items:
  - Idly (Rs 30)
  - Dosa (Rs 50)
  - Biryani (Rs 180)
  - Fried Rice (Rs 120)
  - Meals (Rs 100)
  - Paneer Curry (Rs 140)
  - Chicken Curry (Rs 170)
  - Ice Cream (Rs 40)
  - Cold Drink (Rs 20)
- Add multiple items to order
- Calculate and process food bill payments

### 5. **Checkout Management**
- Process customer checkout
- Verify room occupancy
- Calculate extra charges for extended stays
- Mark rooms as available after checkout

### 6. **Booking Tracker**
- Display total number of bookings on the main page
- Real-time booking counter

## Room Details

| Room No | Type    | Capacity | Daily Rate |
|---------|---------|----------|-----------|
| 101     | AC      | 2        | Rs 1500   |
| 102     | AC      | 4        | Rs 2200   |
| 201     | Non-AC  | 2        | Rs 1000   |
| 202     | Non-AC  | 3        | Rs 1300   |
| 301     | AC      | 3        | Rs 2000   |
| 302     | Non-AC  | 4        | Rs 1500   |

## System Requirements

- **Python** 3.x
- **Tkinter** (usually comes with Python)
- **Operating System**: Linux, macOS, or Windows
- **Display**: Graphical display environment (X11 for Linux)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Jeevani06/HotelManagement.git
cd HotelManagement
