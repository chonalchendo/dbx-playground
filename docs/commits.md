## Best Practices for Python Commits

- **Verify before committing**: Ensure code passes ruff linting, bandit security checks, and all tests
- **Atomic commits**: Each commit should contain related changes that serve a single purpose
- **Split large changes**: If changes touch multiple concerns, split them into separate commits
- **Conventional commit format**: Use the format `<type>: <description>` where type is one of:
  - `feat`: A new feature
  - `fix`: A bug fix
  - `docs`: Documentation changes
  - `style`: Code style changes (formatting, etc)
  - `refactor`: Code changes that neither fix bugs nor add features
  - `perf`: Performance improvements
  - `test`: Adding or fixing tests
  - `chore`: Changes to dependencies, build process, tools, etc.
  - `ci`: CI/CD improvements
  - `build`: Changes to build system or dependencies
- **Present tense, imperative mood**: Write commit messages as commands (e.g., "add feature" not "added feature")
- **Concise first line**: Keep the first line under 72 characters
- **Emoji**: Each commit type is paired with an appropriate emoji:
  - ✨ `feat`: New feature
  - 🐛 `fix`: Bug fix
  - 📝 `docs`: Documentation
  - 💄 `style`: Formatting/style
  - ♻️ `refactor`: Code refactoring
  - ⚡️ `perf`: Performance improvements
  - ✅ `test`: Tests
  - 🔧 `chore`: Tooling, configuration
  - 🚀 `ci`: CI/CD improvements
  - 🏗️ `build`: Build system changes
  - 🔒️ `fix`: Fix security issues
  - 🚨 `fix`: Fix linter warnings
  - 📦️ `build`: Add or update dependencies
  - ➕ `build`: Add a dependency
  - ➖ `build`: Remove a dependency
  - 🧑‍💻 `chore`: Improve developer experience
  - 🐍 `feat`: Python-specific features
  - 🔍️ `feat`: Improve code analysis or type hints
  - 🏷️ `feat`: Add or update type annotations
  - 🧪 `test`: Add experimental tests
  - 🦺 `feat`: Add input validation or error handling
  - 📊 `feat`: Add logging, monitoring, or analytics
  - 🌍 `feat`: Environment or configuration changes
  - 🗃️ `feat`: Database-related changes
  - 🔐 `feat`: Authentication or authorization features
  - 🎯 `perf`: Optimize algorithms or data structures
  - 🧹 `refactor`: Code cleanup
  - ⚰️ `refactor`: Remove dead code
  - 🚑️ `fix`: Critical hotfix
  - 🩹 `fix`: Simple fix for a non-critical issue
  - 💚 `fix`: Fix CI build
  - 🔥 `refactor`: Remove code or files

## Python-Specific Guidelines for Splitting Commits

When analyzing the diff for Python projects, consider splitting commits based on:

1. **Module separation**: Changes to different Python modules or packages
2. **Functionality**: Core logic vs tests vs documentation vs configuration
3. **Dependencies**: Adding/removing dependencies vs code changes
4. **Type annotations**: Adding type hints as separate commits
5. **Refactoring vs features**: Keep refactoring separate from new functionality
6. **Configuration changes**: pyproject.toml, pre-commit config, CI files
7. **Infrastructure**: Docker, deployment scripts, environment files

## Examples

Good Python commit messages:
- ✨ feat: add user authentication with JWT tokens
- 🐛 fix: resolve memory leak in data processing pipeline
- 📝 docs: add docstrings to core API functions
- ♻️ refactor: simplify error handling in database module
- 🚨 fix: resolve ruff linting warnings in models.py
- 🧑‍💻 chore: update pre-commit hooks configuration
- 🐍 feat: implement async context manager for database connections
- 🩹 fix: handle edge case in string parsing function
- 🚑️ fix: patch critical security vulnerability in auth middleware
- 🔍️ feat: add comprehensive type hints to API endpoints
- 🔥 refactor: remove deprecated utility functions
- 🦺 feat: add input validation for user registration
- 💚 fix: resolve failing pytest tests in CI
- 📊 feat: implement structured logging with correlation IDs
- 🔒️ feat: add rate limiting to API endpoints
- ➕ build: add pydantic dependency for data validation
- 🏷️ feat: add TypedDict definitions for API responses
- 🧪 test: add property-based tests with hypothesis
- 🌍 chore: update environment variables configuration

Example of splitting Python commits:
- First commit: ➕ build: add fastapi and uvicorn dependencies
- Second commit: ✨ feat: implement basic REST API endpoints
- Third commit: 🏷️ feat: add pydantic models for request validation
- Fourth commit: 📝 docs: add API documentation with examples
- Fifth commit: ✅ test: add unit tests for API endpoints
- Sixth commit: 🔧 chore: configure uvicorn for development
- Seventh commit: 🚨 fix: resolve bandit security warnings
- Eighth commit: 🐍 feat: add async database connection pooling
