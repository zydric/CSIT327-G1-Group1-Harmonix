# Harmonix

A web platform designed to connect musicians and bands with opportunities, enabling collaboration, networking, and community building.

## Overview

Harmonix is built with Django and follows a modular, scalable structure to support future feature expansion. The platform provides musicians and bands with tools to showcase their talents and discover new opportunities in the music industry.

## Goals

- Provide a simple and reliable way for musicians and bands to showcase themselves
- Enable discovery and listings of opportunities (e.g., auditions, gigs, collaborations)
- Lay the foundation for scalable features such as user accounts, profiles, and listings

### Installation

1. **Clone the repository**
   ```bash
   git clone <repo_url>
   cd harmonix
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv env
   env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start development server**
   ```bash
   python manage.py runserver
   ```

The application will be available at `http://127.0.0.1:8000/`

## Project Structure

The project follows Django's recommended layout with a focus on modular apps and organized static/template directories.

```
harmonix/
├── harmonix/                # Django project settings and configuration
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── accounts/                # Handles user authentication (login, register)
│   ├── migrations/
│   ├── templates/accounts/
│   │   ├── login.html
│   │   └── register.html
│   ├── static/accounts/
│   │   ├── css/
│   │   │   ├── login.css
│   │   │   └── register.css
│   │   ├── js/
│   │   └── assets/
│   │       └── (logos, svgs, images)
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── apps.py
│
├── musician_profile/        # Musician user profiles
├── band_profile/            # Band user profiles
├── listings/                # Listings and opportunities
│
├── templates/               # Global templates
│   ├── base.html            # Global layout
│   └── navbar.html          # Shared navbar
│
├── static/                  # Global static files
│   ├── css/
│   ├── js/
│   └── assets/
│       └── (shared images, svgs)
│
├── manage.py
└── requirements.txt
```

## Naming Conventions

To maintain consistency across the project:

### Files and Folders
- **Python files & folders** → `snake_case`
- **Django apps** → `snake_case`
- **Templates** → `snake_case.html`
- **Static files** → `snake_case.css`, `snake_case.js`, `snake_case.svg`

### Git
- **Branches** → `type/scope/snake_case_description`
  - Examples: `feature/accounts/user_authentication`, `fix/listings/listings_filter_bug`
- **Commit messages** → Follow [Conventional Commit Messages](#commit-messages-conventional-commits)
  - Examples: `feat(auth): add login endpoint`, `fix(listings): correct filter by genre query`

### In short terms:
- **Branches**&emsp;&emsp;&emsp;&emsp;&emsp;: `type/scope/snake_case_description`
- **Commit messages**&emsp;: `<type>(scope): short description`

### Code
- **Variables** → `snake_case`
- **Classes** → `PascalCase`
- **Constants** → `ALL_CAPS`
- **Django migrations** → Auto-generated (do not rename)
---
## Git Workflow

We use a feature-branch workflow to keep the `main` branch stable.

### Branch Naming
**Format:**
```
type/scope/snake_case_description
```

### Branch Types
- `setup/` → initial project setup (e.g., Django project, `.gitignore`, configs).
- `feature/` → New functionality (apps, views, models, templates, UI components)
- `fix/` → Bug fixes (logic errors, broken views, styling issues)
- `refactor/` → Code improvements without changing behavior
- `chore/` → Maintenance (config, dependencies, cleanup)
- `docs/` → Documentation changes (README, comments, guides)

#### Rule of Thumb:
- If it changes how the system behaves = `feature/`. 
- If it only fixes something broken = `fix/`. 
- If it cleans up without changing behavior = `refactor/`.

### Scope

`scope` is the main component/area of changes:
- `accounts`, `listings` - for app-specific changes
- `project` - for project-wide changes (settings, global templates)  
- `frontend`, `api`, `database` - for layer-specific changes
- Example: `feature/accounts/user_authentication`, `fix/project/static_config`

---
### Commit Messages [(Conventional Commits)](www.conventionalcommits.org)

**Format:**
```
<type>(scope): short description
```

**Common types and examples:**
```bash
feat(accounts): add register endpoint
fix(listings): correct genre filter query
refactor(models): reorganize profile models for clarity
docs(readme): add setup instructions
style(css): normalize navbar spacing
chore(deps): bump Django to 4.x
test(accounts): add login integration test
```

**Guidelines:**
- `(scope)` is the app or area affected (`accounts`, `listings`, `templates`)
- Keep messages present-tense and concise
    - Example: `add` not `added`, `fix` not `fixed`
- One logical change per commit
- Limit commit message titles under 50 characters
- The body of the commit message should be wrapped at 72 characters

---
### Workflow Steps

#### When to Create a Branch
Use `feature/` branch when:
- **New feature** 
- **New app** 
- **New views/templates** 
- **Model/schema changes** 
- **Significant UI work** 

**Bug fixes** → `fix/` branch

**Small fixes** → create a quick branch even for small changes/tweaks
- `hotfix/accounts/fix_typo_login_form`
- `chore/frontend/adjust_button_spacing` 
- Quick to create, keeps changes isolated, easier to review, and keeps main protected

#### Typical Flow
```bash
# Update local main
git checkout main
git pull origin main

# Create feature branch
git checkout -b feature/short_description

# Work, then commit logically (one purpose per commit)
git add .
git commit -m "feat(listings): add listing model"

# Push & open PR
git push origin feature/short_description
# Then open PR on GitHub, request review, and merge after approval

# After merge, sync local main
git checkout main
git pull origin main
```

### Best Practices
- Keep commits atomic (one logical change per commit)
- Provide meaningful commit messages using Conventional Commits format
- PR description should explain what changed and how to test
- At least one reviewer must approve before merging to `main`

---
## Static File Organization

### Structure & Naming Rules

Each app should include its own `css`, `js`, and `assets` folders. Global shared assets go under `static/`.

**Per-app structure:**
```
accounts/
└── static/
    └── accounts/
        ├── css/
        │   └── login.css
        ├── js/
        │   └── login.js
        └── assets/
            └── logo.svg
```

**Global structure:**
```
static/
├── css/
│   └── base.css
├── js/
│   └── base.js
└── assets/
    └── logo.svg
```

### Naming Guidelines
- Filenames in `snake_case`: `band_card_bg.svg`, `musician_avatar_placeholder.png`
- Prefer `assets/` directory (covers SVGs, PNGs, icons, fonts)
- Always reference static files with Django's `{% static %}` tag (do not hardcode `/static/` paths)
---
## Contribution Guidelines

- Follow the Git workflow described above
- Keep changes modular — one feature/fix per branch
- Write clear, descriptive commit messages using Conventional Commits
- Ensure code follows the established naming conventions
- Test your changes before submitting a PR
- Do not commit environment files (`.env`) or virtual environment directories (`env/`)
- Do not commit IDE-specific files (`.vscode/`, `.idea/`, etc.)
---
## Final Notes
> Always branch off `main` and run `git status` before every add, commit, or push.

> If you’re unsure, run `git status`. It’s your safety net.