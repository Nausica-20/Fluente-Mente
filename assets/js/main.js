/**
 * Fluente-Mente
 * Main JavaScript
 *
 * Handles the mobile navigation.
 */

document.addEventListener("DOMContentLoaded", function () {
  const toggle = document.querySelector(".nav-toggle");
  const menu = document.querySelector(".nav-menu");

  if (!toggle || !menu) {
    return;
  }

  function openMenu() {
    menu.classList.add("is-open");
    toggle.setAttribute("aria-expanded", "true");
  }

  function closeMenu() {
    menu.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");
  }

  function isMenuOpen() {
    return menu.classList.contains("is-open");
  }

  // Toggle mobile menu
  toggle.addEventListener("click", function () {
    if (isMenuOpen()) {
      closeMenu();
    } else {
      openMenu();
    }
  });

  // Close menu when a navigation link is clicked
  const navLinks = menu.querySelectorAll(".nav-link");

  navLinks.forEach(function (link) {
    link.addEventListener("click", function () {
      closeMenu();
    });
  });

  // Close menu with Escape
  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && isMenuOpen()) {
      closeMenu();
      toggle.focus();
    }
  });

  // Close menu when clicking outside the navigation
  document.addEventListener("click", function (event) {
    const navigation = document.querySelector(".site-nav");

    if (!navigation) {
      return;
    }

    if (isMenuOpen() && !navigation.contains(event.target)) {
      closeMenu();
    }
  });

  // Reset mobile menu when returning to desktop
  window.addEventListener("resize", function () {
    if (window.innerWidth > 1024) { 
      closeMenu();
    }
  });
});
