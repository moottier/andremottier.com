const bulmaActive = 'is-active'

document.addEventListener('DOMContentLoaded', (event) => {
    const menuBurger = document.getElementById('navbarMenuButtonBurger');
    const menu = document.getElementById('navbarMenuHeroA')
    menuBurger.addEventListener('click', function(){
        menu.classList.toggle(bulmaActive);
        menuBurger.classList.toggle(bulmaActive);
    });
    menu.addEventListener('click', function(){
        menu.classList.toggle(bulmaActive);
        menuBurger.classList.toggle(bulmaActive);
    });
});