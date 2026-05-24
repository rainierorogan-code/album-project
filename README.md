# MLBB Hall of Fame — Digital Archive

MLBB Hall of Fame is a Mobile Legends: Bang Bang (MLBB) themed digital archive designed for players to organize and showcase their battle records, gameplay highlights, and collection assets.  

The platform acts as a personal "Hall of Fame" where users can curate, manage, and display their achievements through an immersive game-inspired interface inspired by the official MLBB client design.

---

# Live Website

🌐 Live Demo: https://album-project-c9js.onrender.com

---

# GitHub Repository

📁 GitHub Repository: https://github.com/rainierorogan-code/album-project.git

---

# Project Overview

The application provides a modern esports-inspired experience that allows players to:

- Store gameplay screenshots
- Archive battle records
- Showcase highlights
- Organize personal MLBB collections
- Manage custom albums and records

The entire platform is designed around the visual identity of Mobile Legends: Bang Bang using metallic gold accents, deep navy backgrounds, glowing hover effects, and bold typography.

---

# Tech Stack

## Backend
- Django (Python)

Handles:

- User authentication
- Database management
- Asset management
- Administrative controls
- Backend security

---

## Frontend
- Tailwind CSS

Used to create:

- MLBB-inspired user interface
- Responsive layouts
- Dynamic hover effects
- Mythic-themed design system

---

## Database
- SQLite (Development)
- PostgreSQL (Production)

Stores:

- User profiles
- Album titles
- Descriptions
- Metadata
- User collections

---

## Media Storage
- Cloudinary

Provides:

- Cloud image hosting
- Optimized image delivery
- Remote asset storage
- High-quality screenshot management

---

## Deployment
- Render.com

Used for:

- Cloud hosting
- Production deployment
- Database hosting
- Environment variable management

---

## Version Control
- GitHub

Used for:

- Source code management
- Collaboration
- Version tracking
- Deployment integration

---

# Core Features

## Esports-Ready Interface
Every screen is designed with a consistent MLBB-inspired visual style featuring:

- Metallic gold highlights
- Deep navy backgrounds
- Bold uppercase typography
- Mythic-themed user interface
- Animated hover glow effects

---

## Secure User Authentication
Users can:

- Register accounts
- Log in securely
- Manage personal collections
- Access private galleries

Each user maintains their own isolated archive system.

---

## Dynamic Collection Management
Players can:

- Initialize battle records
- Modify existing entries
- Terminate outdated records
- Upload gameplay assets
- Organize custom collections

---

## Role-Based Access Control (RBAC)
The system includes administrator-level controls for:

- Global monitoring
- User management
- Content auditing
- Platform administration

---

## Responsive Asset Gallery
The archive includes a responsive grid-based gallery system that:

- Dynamically updates user content
- Displays uploaded screenshots
- Supports hover-state glow effects
- Mimics legendary in-game item visuals

---

## Cloud-Synchronized Media Storage
Cloudinary integration allows:

- Fast image delivery
- Reliable media hosting
- Automatic cloud synchronization
- Lightweight application performance

---

# Conceptual Architecture

The platform operates using a client-server architecture.

## Frontend Layer
Handles:

- User interface rendering
- Responsive layouts
- User interaction
- MLBB-inspired visual presentation

---

## Backend Layer
Handles:

- Authentication
- Database queries
- Access control
- Business logic
- CRUD operations

---

## Cloud Storage Layer
Cloudinary acts as the remote repository for uploaded assets and gameplay screenshots.

---

# Security Features

The application implements Role-Based Access Control (RBAC) to protect user content.

## Standard Users
Regular users can:

- Manage personal archives
- Upload screenshots
- Edit collections
- Delete their own records

---

## Administrators
Administrators can:

- Monitor all user content
- Audit platform uploads
- Manage system-wide records

---

# Getting Started

## 1. Install Project Requirements

```bash
pip install -r requirements.txt
```

---

## 2. Configure Environment Variables

Create a `.env` file and add:

```env
SECRET_KEY=your_secret_key

DEBUG=True

DATABASE_URL=your_postgresql_database_url

CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

---

## 3. Apply Database Migrations

```bash
python manage.py migrate
```

---

## 4. Create an Administrator Account

```bash
python manage.py createsuperuser
```

---

## 5. Run the Development Server

```bash
python manage.py runserver
```

Visit:

```text
http://127.0.0.1:8000/
```

---

# Deployment Configuration

## Render Build Command

```bash
pip install -r requirements.txt && python manage.py migrate
```

---

## Render Start Command

```bash
gunicorn core.wsgi:application
```

---

# Cloudinary Asset Management

## Automatic Media Cleanup
Uploaded assets are automatically removed from Cloudinary whenever records are deleted from the system.

---

## Manual Asset Management
To manually manage uploaded files:

1. Open the Cloudinary Dashboard
2. Navigate to **Media Explorer**
3. Select uploaded assets
4. Click **Delete**

---

# Testing Scenarios

## Standard User Verification

1. Create a user account
2. Upload gameplay screenshots
3. Create battle records
4. Log in using another account
5. Verify that user archives remain private

---

## Administrator Verification

1. Log in using an administrator account
2. Access the administrative dashboard
3. Verify visibility of all uploaded records

---

# Project Goal

MLBB Hall of Fame — Digital Archive was developed to provide Mobile Legends players with a modern, secure, and visually immersive platform for archiving and showcasing their in-game achievements, battle records, and gameplay highlights.
