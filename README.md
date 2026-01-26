# 🚀 Pranav's Full-Stack Portfolio

Welcome to my professional portfolio! This project showcases my skills as a Full-Stack Developer, specializing in the MERN stack, Python, and robust web engineering.

![Portfolio Preview](seo.png)

## 🌟 Features

- **Dynamic UI**: Modern, responsive design with a glassmorphic aesthetic and smooth animations.
- **Typing Effect**: Interactive hero section highlighting core roles.
- **Contact System**: Integrated Flask & MongoDB backend for handling form submissions.
- **Dockerized**: Fully containerized application for consistent development and deployment.
- **Automation**: Includes scripts and CI/CD pipelines for streamlined workflows.

## 🛠️ Tech Stack

- **Frontend**: HTML5, Vanilla CSS, JavaScript (ES6+), Google Fonts.
- **Backend**: Python (Flask), Flask-CORS.
- **Database**: MongoDB.
- **DevOps**: Docker, Docker Compose, GitHub Actions.
- **Tools**: Makefile, Batch scripts.

## 🚀 Getting Started

### Prerequisites

- [Docker and Docker Compose](https://docs.docker.com/get-docker/) installed.

### Fast Track (Windows)

Simply double-click the `run.bat` file in the root directory. This will open an interactive menu to:

1. Build and Start the application.
2. View real-time logs.
3. Stop the containers.
4. Perform a full cleanup.

### Terminal Method (Cross-Platform)

We use a `Makefile` to simplify common tasks:

```bash
# Build and start everything in the background
make up

# View application logs
make logs

# Stop the containers
make down

# Complete cleanup (remove images and volumes)
make clean
```

The application will be accessible at:

- **Frontend**: Open `index.html` in your browser.
- **Backend**: `http://localhost:5000`

## 📁 Project Structure

```text
.
├── .github/workflows/  # CI/CD pipelines
├── app.py             # Flask Backend
├── Dockerfile          # Docker configuration
├── docker-compose.yml  # Multi-container orchestration
├── index.html          # Main landing page
├── style.css           # Core design system
├── script.js           # Frontend logic
├── requirements.txt    # Python dependencies
├── Makefile            # Automation commands
└── run.bat            # Windows automation script
```

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

Built with ❤️ by [Pranav](https://github.com/toxicbishop)
