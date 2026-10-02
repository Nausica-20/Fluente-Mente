/**
 * Fluente-Mente
 * Main JavaScript
 *
 * Handles the responsive mobile navigation.
 */

document.addEventListener("DOMContentLoaded", function () {
  const toggle = document.querySelector(".nav-toggle");
  const menu = document.querySelector(".nav-menu");
  const navigation = document.querySelector(".site-nav");

  if (!toggle || !menu || !navigation) {
    return;
  }

  function openMenu() {
    menu.classList.add("is-open");
    toggle.setAttribute("aria-expanded", "true");
    toggle.setAttribute("aria-label", "Chiudi il menu");
  }

  function closeMenu() {
    menu.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");
    toggle.setAttribute("aria-label", "Apri il menu");
  }

  function isMenuOpen() {
    return menu.classList.contains("is-open");
  }

  toggle.addEventListener("click", function (event) {
    event.stopPropagation();

    if (isMenuOpen()) {
      closeMenu();
    } else {
      openMenu();
    }
  });

  menu.querySelectorAll(".nav-link").forEach(function (link) {
    link.addEventListener("click", closeMenu);
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && isMenuOpen()) {
      closeMenu();
      toggle.focus();
    }
  });

  document.addEventListener("click", function (event) {
    if (isMenuOpen() && !navigation.contains(event.target)) {
      closeMenu();
    }
  });

  window.addEventListener("resize", function () {
    if (window.innerWidth > 1024 && isMenuOpen()) {
      closeMenu();
    }
  });
});
