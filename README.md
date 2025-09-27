# Harmonix

A web platform designed to connect musicians and bands with opportunities, enabling collaboration, networking, and community building.

## Overview

Harmonix is built with Django and follows a modular, scalable structure to support future feature expansion. The platform provides musicians and bands with tools to showcase their talents and discover new opportunities in the music industry.

## Goals

- Provide a simple and reliable way for musicians and bands to showcase themselves
- Enable discovery and listings of opportunities (e.g., auditions, gigs, collaborations)
- Lay the foundation for scalable features such as user accounts, profiles, and listings

---

## Quick Setup for New Developers

### 1. Clone and Setup Environment
```bash
# Clone the repository
git clone <repo_url>
cd harmonix

# Create virtual environment
python -m venv env

# Activate vitual environment
env\Scripts\activate          

# You should see (env) in your terminal prompt - this is IMPORTANT!
```

### 2. Install Dependencies
```bash
# Make sure you're in the virtual environment (see (env) in prompt)
pip install -r requirements.txt

# If requirements.txt is missing or empty, install Django manually:
pip install django
```

### 3. Database Setup
```bash
python manage.py migrate
python manage.py createsuperuser  # Optional: for admin access
```

### 4. Start Development
```bash
python manage.py runserver
# Visit http://127.0.0.1:8000/
```

### ⚠️ **CRITICAL: Always Activate Virtual Environment**
Every time you start work:
```bash
cd harmonix
env\Scripts\activate    # You MUST see (env) in your prompt
```
**Without (env) showing, Django commands will fail!**

---

## Branch Protection & Workflow Rules

### Main Branch is Protected
- **❌ NO direct commits to `main`** - pushes will be **rejected**
- **✅ ALL changes require Pull Requests** with approval
- **✅ Create branches for EVERY change** - even one-line fixes

### If You Accidentally Commit to Main
Don't panic! Here's how to fix it:
```bash
# 1. Your push will be rejected (this is expected!)
# 2. Move your commit to a new branch:
git checkout -b feature/your-branch-name
git push origin feature/your-branch-name

# 3. Reset main to match remote
git checkout main
git reset --hard origin/main

# 4. Create PR from your new branch
```

---

## Git Workflow & Conventions

### Branch Naming Format
```
type/scope/snake_case_description
```

**Examples:**
```bash
feature/accounts/user_authentication
fix/listings/filter_bug_fix  
chore/project/update_dependencies
docs/readme/improve_setup_guide
```

### Branch Types
| Type | When to Use | Examples |
|------|-------------|----------|
| `feature/` | New functionality, apps, views, models | `feature/accounts/login_system` |
| `fix/` | Bug fixes, broken functionality | `fix/listings/broken_search` |
| `chore/` | Dependencies, configs, maintenance | `chore/project/add_requirements` |
| `docs/` | Documentation, README, comments | `docs/readme/update_workflow` |
| `refactor/` | Code cleanup without behavior change | `refactor/models/simplify_user_model` |

### Scope Guidelines
`scope` indicates where you're making changes:
- **App name** (`accounts`, `listings`) - for app-specific changes
- **`project`** - for project-wide changes (settings, global templates/static)
- **Layer** (`frontend`, `database`, `api`) - when changes span multiple apps

**Examples:**
- `feature/accounts/password_reset` - changes only in accounts app
- `feature/project/add_global_navbar` - affects entire project
- `fix/frontend/responsive_layout` - CSS/styling across multiple apps

### Commit Messages (Conventional Commits)
**Format:** `<type>(scope): lowercase description`

```bash
# Good examples:
feat(accounts): add user registration endpoint
fix(listings): resolve search filter bug
chore(deps): update django to 4.2
docs(readme): improve installation steps
style(frontend): fix navbar spacing
refactor(models): simplify user profile structure

# Bad examples:
Fixed bug                    # Too vague, wrong format
feat(accounts): Added login  # Should be lowercase, present tense
Update README               # Missing type and scope
```

### Commit Guidelines
- **Present tense:** `add` not `added`, `fix` not `fixed`
- **Lowercase description:** after the colon
- **One logical change per commit** (atomic commits)
- **Commit early and often** - even for small changes
- **Under 50 characters** for the title
- The **body** of the commit message should be wrapped at **72 characters**

---

## Daily Workflow

### Starting Work
```bash
# 1. Always start fresh
git checkout main
git pull origin main

# 2. Activate virtual environment
env\Scripts\activate        # See (env) in prompt!

# 3. Create feature branch
git checkout -b feature/scope/your_task

# 4. Work on your changes...
```

### Making Changes
```bash
# Check status frequently - your safety net!
git status

# Stage and commit atomically
git add specific_file.py          # Stage specific files
git commit -m "feat(accounts): add user model"

# Or stage all changes
git add .
git commit -m "style(frontend): improve responsive design"
```

### Submitting Changes
```bash
# Push your branch
git push origin feature/scope/your_task

# Go to GitHub → Create Pull Request
# Wait for approval → Merge
```

### After Merge
```bash
# Sync your local main
git checkout main
git pull origin main

# Delete old feature branch (optional)
git branch -d feature/scope/your_task
```

---

## 📁 Project Structure

```
harmonix/
├── manage.py
├── requirements.txt
├── harmonix/                # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── accounts/                # User authentication app
│   ├── migrations/
│   ├── templates/accounts/  # App-specific templates (namespaced)
│   │   ├── login.html
│   │   └── register.html
│   ├── static/accounts/     # App-specific static files (namespaced)
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── views.py
│   ├── urls.py
│   └── models.py
│
├── templates/               # Global templates
│   └── base.html
│   
│
└── static/                  # Global static files
    ├── css/
    │   └── base.css
    ├── js/
    │   └── main.js
    └── images/
        └── logo.png
```

### App Structure Rules
Each Django app should contain:
- **Templates:** `app_name/templates/app_name/` (namespaced)
- **Static files:** `app_name/static/app_name/` (namespaced)
- **Standard files:** `views.py`, `urls.py`, `models.py`, `apps.py`

### Global vs App-Level Files
**Global files** (project root):
- Base templates (`base.html`, error pages)
- Site-wide CSS/JS
- Shared images (logos, icons)

**App-level files** (within apps):
- App-specific templates
- Feature-specific styling
- App-related images

---

## Naming Conventions

### Files & Folders
- **Python files:** `snake_case.py`
- **Templates:** `snake_case.html`
- **Static files:** `snake_case.css`, `snake_case.js`
- **Django apps:** `snake_case`
- **Variables:** `snake_case`
- **Classes:** `PascalCase`
- **Constants:** `ALL_CAPS`

### Examples
```python
# Good
user_profile.py
login_form.html
base_styles.css
class UserProfile(models.Model):
    first_name = models.CharField()
    ROLE_CHOICES = [...]

# Bad
UserProfile.py
loginForm.html  
baseStyles.css
class user_profile(models.Model):
    firstName = models.CharField()
```

---

## Django Settings & Configuration

### Static Files Setup
**In templates, always use:**
```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/base.css' %}">
<script src="{% static 'js/main.js' %}"></script>
```

**Never hardcode paths:**
```html
<!-- ❌ Bad -->
<link rel="stylesheet" href="/static/css/base.css">

<!-- ✅ Good -->
<link rel="stylesheet" href="{% static 'css/base.css' %}">
```

### Important: URL Slashes
In `settings.py`, trailing slash is **required** for `STATIC_URL`:
```python
STATIC_URL = '/static/'  # ✅ Correct - both leading and trailing slashes
STATIC_URL = 'static/'   # ❌ Wrong - missing leading slash
STATIC_URL = '/static'   # ❌ Wrong - missing trailing slash
```

---

## Testing Your Changes

Before creating a PR:
```bash
# 1. Activate virtual environment
env\Scripts\activate

# 2. Run the development server
python manage.py runserver

# 3. Test your changes at http://127.0.0.1:8000/

# 4. Check for any errors in terminal

# 5. Make sure templates and static files load correctly
```

---

## ⚠️ Common Pitfalls & How to Avoid Them

### Virtual Environment Issues
**Problem:** Django commands fail with "No module named django"

**Solution:** Always activate your virtual environment first
```bash
env\Scripts\activate  # Must see (env) in prompt!
```

### Direct Main Commits
**Problem:** Push to main gets rejected

**Solution:** Always create feature branches
```bash
# Never do this:
git checkout main
git add .
git commit -m "changes"
git push origin main  # ❌ Will be rejected!

# Always do this:
git checkout -b feature/scope/description
git add .
git commit -m "feat(scope): description"
git push origin feature/scope/description  # ✅ Correct
```

### Static Files Not Loading
**Problem:** CSS/JS files return 404 errors

**Solution:** Use `{% static %}` tag and check file paths
```html
<!-- ❌ Wrong -->
<link rel="stylesheet" href="/static/css/style.css">

<!-- ✅ Correct -->
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

---

## 📚 Essential Commands Reference

### Virtual Environment
```bash
# Create (one time only)
python -m venv env

# Activate (every time you start work)
env\Scripts\activate          # Windows

# Deactivate when you're done for the day
deactivate
```

### Django Commands
```bash
# Start development server
python manage.py runserver

# Create new app
python manage.py startapp app_name

# Database migrations
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser
```

### Git Commands
```bash
# Check current status (use frequently!)
git status

# Check current branch
git branch

# Create and switch to new branch
git checkout -b feature/scope/description

# Stage changes
git add .                    # All changes
git add specific_file.py     # Specific file

# Commit with message
git commit -m "feat(scope): description"

# Push branch
git push origin branch-name

# Switch branches
git checkout main
git checkout feature/branch-name

# Pull latest changes
git pull origin main
```

---

## 🎯 Final Notes & Best Practices

### Always Remember
- `git status` is your best friend - use it constantly
- **Check your branch** before making changes: `git branch`
- **Activate virtual environment** every session: look for `(env)`
- **Never work directly on main** - always create feature branches
- **Commit small and often** - better than large, complex commits
- **Test your changes** before pushing

### Before Every Work Session
```bash
cd harmonix                   # Navigate to project
env\Scripts\activate          # Activate virtual environment
git status                    # Check current state
git checkout main             # Switch to main
git pull origin main          # Get latest changes
git checkout -b feature/...   # Create new feature branch
```

### Before Every Commit
```bash
git status                    # See what you're committing
python manage.py runserver    # Test that everything works
git add .                     # Stage your changes
git commit -m "type(scope): description"  # Commit with good message
```

### Pro Tips
- Use **descriptive branch names** - you'll thank yourself later
- **Small commits** are easier to review and debug
- **Ask for help** if you're unsure about something
- **Review your own PR** before asking others to review
- **Keep learning** - Django documentation is excellent

---

> **Remember:** When in doubt, run `git status`. It's your safety net and will show you exactly where you are and what's changed.

> **Golden Rule:** Better to create too many small branches than to work directly on main or create massive commits.

Happy coding! 🎵🚀