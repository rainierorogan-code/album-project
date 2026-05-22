LMSY Gallery Vault — Curated Media System
A secure, warm-minimalist photo sanctuary engineered with Django, PostgreSQL, and Cloudinary for decentralized asset storage. This platform implements strict native backend Role-Based Access Control (RBAC) to isolate user environments and secure media streams.

🚀 Presentation & Grading Quick Start
To streamline evaluation, the system interface features an embedded Grading & RBAC Verification Panel right on the authentication gateway page.

👥 Test Scenarios & Authorization Credentials
Standard User Layer (Isolated Workspace)

Action: Click "Create one here" on the landing interface to register a fresh profile.

RBAC Enforcement: Any public registration defaults to standard user parameters (is_staff=False). Users operate in absolute data isolation—they can only create, view, modify, or delete media parameters that they personally initialized.

System Administrator Layer (Global Oversight)

Username: admin_user

Security Override: Logging in with this master profile lifts localized filters, allowing complete system auditing, object tracking, and administrative access via the interface and the native engine dashboard at /admin.

🛡️ Core Security & RBAC Architecture
The platform implements a multi-layered defense matrix to ensure complete database integrity and block horizontal privilege escalation:

Query-Level Separation: Views inherit LoginRequiredMixin and explicitly override get_queryset() to intercept raw database hits using the active session parameters:

Python
def get_queryset(self):
    if self.request.user.is_superuser:
        return Album.objects.all()
    return Album.objects.filter(created_by=self.request.user)
URL Manipulation Protection: Destructive actions (UpdateView and DeleteView) bind UserPassesTestMixin alongside strict query filters. If an unprivileged user manually alters a URL routing parameter to guess another user's asset ID, the engine automatically returns a clean 404 Not Found or 403 Forbidden intercept block.

Session Integrity & Automatic Bouncing: Unauthenticated traffic or terminated sessions are intercepted at the template header layer and gracefully routed back to the authentication gateway, preventing empty layout leaks.

📂 System File Architecture
Plaintext
photo-album-project/
│
├── core/                         # Project Configuration Root
│   ├── settings.py               # Database tracking & Cloudinary API configuration
│   └── urls.py                   # Main URL routing mappings
│
├── albums/                       # Core Application Folder
│   ├── models.py                 # Album schemas and database definitions
│   └── views.py                  # Strict RBAC query isolation filters
│
└── templates/                    # Centralized Layouts Engine
    ├── albums/
    │   ├── base.html             # Global canvas container with session intercepts
    │   └── album_list.html       # Dynamic personalized gallery feed
    └── registration/
        ├── login.html            # Gateway interface with evaluation guide
        └── signup.html           # Minimalist registration terminal
🛠️ Technical Tech Stack
Core Framework: Django 5.x (Python)

Database Management System: PostgreSQL (Production on Render) / SQLite (Local Fallback)

Cloud Infrastructure Sync: Cloudinary API SDK (cloudinary_storage Integration)

Asset Servicing Middleware: WhiteNoise (Compressed Manifest Static Storage)

UI Interface Layout: Tailwind CSS via CDN (Warm-minimalist aesthetic)

📦 Local Deployment Workflow
To mirror this platform on a local station, execute the following routines inside your workspace terminal:

1. Initialize Environment Variables
Create a .env file within the root workspace directory and map your respective server parameters:

Code snippet
DJANGO_SECRET_KEY=your_local_secret_key
DJANGO_DEBUG=True
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
2. Dependency Resolution & Database Execution
Install package requirements, build your local database schemas, and initialize the development server:

Bash
# Install system libraries
pip install -r requirements.txt

# Compile database configurations
python manage.py makemigrations
python manage.py migrate

# Boot up the local runtime engine
python manage.py runserver
Navigate to http://127.0.0.1:8000/ to preview the interface workspace locally.

🌐 Production Environment Controls (Render)
The platform tracking branches map automatically to production clusters. The application pipeline depends on these core deployment configurations:

Build Command: pip install -r requirements.txt && python manage.py migrate

Start Command: gunicorn core.wsgi:application

Database Tracking Rule: Handled dynamically via dj_database_url matching against a persistent DATABASE_URL environment flag. If the variable is present, local temporary SQLite states are disabled to enforce permanent storage.
