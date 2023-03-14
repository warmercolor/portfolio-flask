/* Opens and closes side menu in mobile mode */
const menuMobile = document.querySelector('.menu-mobile')
const body = document.querySelector('body')

menuMobile.addEventListener('click', () => {
    menuMobile.classList.contains('bi-list')
    ? menuMobile.classList.replace('bi-list', 'bi-x')
    : menuMobile.classList.replace('bi-x", "bi-list')

    body.classList.toggle('menu-nav-active')
})

/* Close the menu when clicking on an item and change the icon to list */
const navItem = document.querySelectorAll('.nav-item');

navItem.forEach((item) => {
    item.addEventListener('click', () => {
        if (body.classList.contains('menu-nav-active')) {
            body.classList.remove('menu-nav-active')
            menuMobile.classList.replace('bi-x', 'bi-list')
        }
    })
})
