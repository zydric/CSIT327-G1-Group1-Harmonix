# Harmonix

A web platform designed to connect musicians and bands with opportunities, enabling collaboration, networking, and community building.

## Goals

- Provide a simple and reliable way for musicians and bands to showcase themselves
- Enable discovery and listings of opportunities (e.g., auditions, gigs, collaborations)
- Lay the foundation for scalable features such as user accounts, profiles, and listings

---

## Tech Stack

- **Backend:** Django (Python web framework)
- **Database:** Supabase (PostgreSQL)
- **Frontend:** Tailwind CSS
- **Hosting:** Render

## Team Members

| Name | Role | Email |
|------|------|-------|
| Zydric Abel | Lead Developer | zydric.abel@cit.edu |
| Zander Aligato | Backend Developer | zander.aligato@cit.edu |
| Treasure Louise Abadinas | Frontend Developer | treasurelouise.abadinas@cit.edu |

## Deployed Application

**Live Demo:** [Harmonix on Render - Coming Soon]

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
# 1. Make sure you're in the virtual environment (see (env) in prompt)
pip install -r requirements.txt

# 2. Create a new file named .env in the project root (same folder as manage.py) 
#    and paste the DATABASE_URL in that file.
```

### 3. Database Setup
```bash
python manage.py migrate
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

## Contributing

For detailed information about our development workflow, git conventions, coding standards, and best practices, please see our [**CONTRIBUTING.md**](CONTRIBUTING.md) guide.

This includes:
- Branch naming conventions and workflow rules
- Commit message standards
- Daily development workflow
- Project structure guidelines
- Common pitfalls and solutions
- Essential commands reference

---

## License

This project is developed as part of an academic coursework.
