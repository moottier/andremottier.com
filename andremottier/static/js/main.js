// bulma constants
const bulmaActive = 'is-active';

// query selectors
const bulmaNavbarDropdownLinkSelector = '#navbarMenuHeroA .navbar-start .navbar-item.has-dropdown .navbar-link';

document.addEventListener('DOMContentLoaded', (event) => {

    // init
    const dropdownLink = document.querySelector(bulmaNavbarDropdownLinkSelector);
    const dropdownUrlDefault = dropdownLink.href;
    dropdownLink.addEventListener('click', function(){    // click to show/hide burger submenus
        dropdownLink.parentElement.classList.toggle(bulmaActive);
    });

    if (!isHamburgerActive()) {
        dropdownLink.href = dropdownUrlDefault;
    } else {
        dropdownLink.href = "javascript:;";
    }

    // hide bulma burger submenus on screen resize
    window.addEventListener('resize', function() {
        if (!isHamburgerActive()) { 
            dropdownLink.parentElement.classList.remove(bulmaActive);
            dropdownLink.href = dropdownUrlDefault;
        } else {
            dropdownLink.href = "javascript:;";
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
