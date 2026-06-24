# My - Full Stack Developer Portfolio

This is the source code for my professional portfolio website, built using modern web technologies focusing on performance, scalability, and exceptional user experience.

## 🚀 Tech Stack

- **Frontend**: Next.js 14, React, TypeScript, Tailwind CSS
- **Backend**: Express.js, Flask, Node.js
- **Database**: MySQL, MongoDB, SQLAlchemy, Supabase
- **Animations**: Framer Motion, Three.js
- **Dev Tools**: Git, GitHub, Vercel, VS Code, Vite

## 🛠️ Features

- **Space Themed UI**: Immersive 3D background effects using Three.js and StarBackground.
- **Project Showcase**: Detailed view of my recent works and technical contributions.
- **Skills Section**: Categorized view of my proficiency across Frontend, Backend, and Development Tools.
- **About Me**: Professional bio highlighting my software engineering foundation.
- **Responsive Design**: Fully optimized for mobile, tablet, and desktop devices.
- **Contact**: Direct links to my professional social profiles and email.

## 📦 Getting Started

1. **Clone the repository**:

   ```bash
   git clone https://github.com/toxicbishop/New-Portfolio.git
   ```

2. **Install dependencies**:

   ```bash
   pnpm install
   ```

3. **Run the development server**:

   ```bash
   pnpm run dev
   ```

4. **Open the site**:
   Navigate to [http://localhost:3000](http://localhost:3000)

5. **Personalize Resume**:
   Upload your own resume in the `public/` directory (e.g., as `resume.pdf`) and update the relevant links in the components (such as `Navbar` or `HeroContent`) to point to your file.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

&copy; 2026 Pranav Arun. All rights reserved.

---

# 🚀 Full-Stack Portfolio

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

### 📄 Personalization

To use the "Download Resume" feature, you must add your own resume file:

1. Name your file `resume.pdf`.
2. Place it in the root directory of this project.
3. This file is ignored by Git to keep your personal information private.

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

This project is licensed under the **MIT License** - see the [MIT License](LICENSE) file for details, Built by [Pranav](https://github.com/toxicbishop)
