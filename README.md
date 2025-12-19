# Book Recommendations API

A Flask API that provides random book recommendations from a MongoDB database.

## Description

Scraping from a reading tracker app, we collect the data and save it in a mongodb. The data we save is what you see when you load a recommendation.

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- MongoDB (local installation or MongoDB Atlas account)

## Local Setup

### 1. Create a virtual environment

```bash
python3 -m venv venv
```

### 2. Activate the virtual environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Copy the example environment file:
```bash
cp .env.example .env
```

Edit `.env` and add your MongoDB credentials:

**For local MongoDB:**
```
MONGODB_URI=mongodb://localhost:27017/
MONGODB_DB=book_recommendations
```

**For MongoDB Atlas (cloud):**
```
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/
MONGODB_DB=book_recommendations
```

**Note:** Your MongoDB collections should contain documents with `title` (string) and `cover` (URL string) fields.

## Running the Application

Start the Flask development server:
```bash
flask run
```

The API will be available at `http://localhost:5000`

