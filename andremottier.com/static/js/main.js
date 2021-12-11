// bulma constants
const bulmaActive = 'is-active';

// query selectors
const bulmaNavbarDropdownLinkSelector = '#navbarMenuHeroA .navbar-start .navbar-item.has-dropdown .navbar-link';

document.addEventListener('DOMContentLoaded', (event) => {
    // click to show/hide burger submenus
    const dropdownLink = document.querySelector();
    dropdownLink.addEventListener('click', function(){
        dropdownLink.parentElement.classList.toggle(bulmaActive);
    });

    // hide bulma burger submenus on screen resize
    window.addEventListener('resize', function() {
        if (!isHamburgerActive()) { 
            dropdownLink.parentElement.classList.remove(bulmaActive);
        }
    });

    // click to show/hide burger menu top level
    const menuBurger = document.getElementById('navbarMenuButtonBurger');
    const menu = document.getElementById('navbarMenuHeroA');
    menuBurger.addEventListener('click', function(){
        menu.classList.toggle(bulmaActive);
        menuBurger.classList.toggle(bulmaActive);
        dropdownLink.parentElement.classList.remove(bulmaActive);
    });
});

function hideBulmaDropdown(elBulmaDropdownLink) {
    /**
     * Hides dropdown associated with elBulmaDropdownLink element
     * 
     * @param {element} elBulmaDropdownLink dropdown menu link element
     * @return {nothing} 
     */
    elBulmaDropdownLink.parentElement.classList.remove(bulmaActive);
}

function getHamburgerBreakpointWidth() {
    /**
     * Returns maximum width in pixels where hamburger menu is visible
     *
     * @return {number} window inner width in pixels
     */
    const hamburgerWidthVarName = '--navbarBreakpoint';
    let width = getComputedStyle(document.documentElement).getPropertyValue(hamburgerWidthVarName);
    width = width.replace("px", "");
    return width;
};

function isHamburgerActive() {
    /**
     * Returns true if hamburger menu is active
     *
     * @return {boolean} is hamburger menu active
     */
    let screenWidth = window.screen.width;
    let breakpoint = getHamburgerBreakpointWidth();
    return screenWidth < breakpoint;
}
