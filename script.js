// --- SCROLL TO TOP LOGIC ---

// 1. Get the button
const mybutton = document.getElementById("scrollTopBtn");

// 2. When the user scrolls down 200px, show the button
window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  // Safety check: ensure button exists before trying to style it
  if (!mybutton) return;

  if (
    document.body.scrollTop > 200 ||
    document.documentElement.scrollTop > 200
  ) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// 3. When the user clicks the button, scroll to top
if (mybutton) {
  mybutton.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
}

// --- TYPING EFFECT ---
const typingTextElement = document.getElementById("typing-text");
const roles = [
  "Full-Stack Developer",
  "MERN Stack Specialist",
  "Software Engineer",
  "Problem Solver",
];
let roleIndex = 0;
let charIndex = 0;
let isDeleting = false;

function typeEffect() {
  const currentRole = roles[roleIndex];

  if (isDeleting) {
    typingTextElement.textContent = currentRole.substring(0, charIndex - 1);
    charIndex--;
  } else {
    typingTextElement.textContent = currentRole.substring(0, charIndex + 1);
    charIndex++;
  }

  let typeSpeed = isDeleting ? 100 : 200;

  if (!isDeleting && charIndex === currentRole.length) {
    typeSpeed = 2000; // Pause at end
    isDeleting = true;
  } else if (isDeleting && charIndex === 0) {
    isDeleting = false;
    roleIndex = (roleIndex + 1) % roles.length;
    typeSpeed = 500;
  }

  setTimeout(typeEffect, typeSpeed);
}

// Start typing effect if element exists
if (typingTextElement) {
  document.addEventListener("DOMContentLoaded", typeEffect);
}

// --- TOAST NOTIFICATION ---
function showToast(message) {
  let toast = document.getElementById("toast");
  if (!toast) {
    toast = document.createElement("div");
    toast.id = "toast";
    document.body.appendChild(toast);
  }
  toast.textContent = message;
  toast.className = "show";
  setTimeout(function () {
    toast.className = toast.className.replace("show", "");
  }, 3000);
}

// Copy email helper used by footer "Let's Connect" button
function copyEmail(email) {
  if (!navigator.clipboard) {
    showToast("Copy not supported. Email: " + email);
    return;
  }
  navigator.clipboard.writeText(email).then(
    () => {
      showToast("Email copied to clipboard!");
    },
    (err) => {
      showToast("Failed to copy email.");
      console.error(err);
    },
  );
}
