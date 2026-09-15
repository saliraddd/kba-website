const menuButton = document.getElementById("menuButton");
const mainNav = document.getElementById("mainNav");

if (menuButton && mainNav) {

    menuButton.addEventListener("click", () => {

        mainNav.classList.toggle("active");

    });

}


/* Services Dropdown */

const dropdownToggle = document.querySelector(".dropdown-toggle");
const navDropdown = document.querySelector(".nav-dropdown");

if (dropdownToggle && navDropdown) {

    dropdownToggle.addEventListener("click", (event) => {

        event.preventDefault();
        event.stopPropagation();

        navDropdown.classList.toggle("open");

    });

}