# Book Recommendations API

A Flask API that provides book recommendations from your StoryGraph reading list.

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

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

Edit `.env` and add your credentials:
```
COOKIE=your_cookie_here
UNAME=your_username_here
```

## Running the Application

Start the Flask development server:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

