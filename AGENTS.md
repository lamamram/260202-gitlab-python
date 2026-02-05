# AGENTS.md - Development Guidelines for AI Coding Agents

## Project Overview

Python project implementing a FastAPI REST API serving resources from SQLAlchemy models with SQLite database.

## Build/Lint/Test Commands

* MUST activer mon environnement virtuel en powershell: `& "c:/Users/Admin stagiaire.DESKTOP-8967908/.venv/v_env_260126/Scripts/Activate.ps1"` avant d'installer des packages

### Running the Application

* dans un powershell, dans le dossier racine, lancer la commande:
  + `python main.py`

### Testing

* lancer les tests pytest:
  + `pytest` dans le dossier racine

### Code Quality

* Formatter avec Ruff: `ruff check app/` et `ruff format app/`
* Lint avec Ruff: `ruff check --fix app/`

## File Structure

- modèles SqlAlchemy dans .\app\models
- schémas Pydantic dans .\app\schemas  
- tests pytest dans .\app\tests
- routes FastAPI dans .\app\routes
- configuration Ruff dans .\app\.ruff.toml
- dépendances dans .\app\requirements.txt

## Code Style Guidelines

### Type Hints
- Use type hints for all function parameters and return values
- Example: `def get_temperature(city: str) -> str:`
- Use proper docstrings with Args and Returns sections

### Error Handling
- Use try-except blocks for user input operations
- Handle keyboard interrupts gracefully
- Provide clear error messages in French when appropriate
- Example: `print("Impossible de retirer cette somme ou votre solde est insuffisant.")`

### Module Organization
- Keep modules focused and single-purpose
- Use `__init__.py` for proper package structure
- Export only necessary functions from modules
- Use proper module-level organization

### Coding Standards
- Follow PEP 8 style guidelines
- Avoid global variables - use class attributes or function parameters
- Use proper function signatures with default values where appropriate
- Implement proper validation for user inputs

### Development Workflow
1. Test imports and basic functionality before adding complex features
2. Use proper error handling for all user interactions
3. Run tests and code quality checks before committing
4. Use Ruff for formatting and linting

## Environment Setup
- Python 3.9+ required (Ruff target version)
- Dependencies: `app/requirements.txt`
- Code formatting: Ruff configured in `app/.ruff.toml`