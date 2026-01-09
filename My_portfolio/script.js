// --- DARK MODE LOGIC ---

// 1. Select the button
const toggleButton = document.getElementById("theme-toggle");
const body = document.body;

// 2. Check for saved user preference on page load
if (localStorage.getItem("theme") === "dark") {
  body.classList.add("dark-mode");
  if (toggleButton) toggleButton.textContent = "☀️ Light Mode";
}

// 3. Listen for a click (only if button exists)
if (toggleButton) {
  toggleButton.addEventListener("click", () => {
    // Toggle the class
    body.classList.toggle("dark-mode");

    // Update the button text and SAVE the preference
    if (body.classList.contains("dark-mode")) {
      toggleButton.textContent = "☀️ Light Mode";
      localStorage.setItem("theme", "dark"); // Save to memory
    } else {
      toggleButton.textContent = "🌙 Dark Mode";
      localStorage.setItem("theme", "light"); // Save to memory
    }
  });
}

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
