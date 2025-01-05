const navStartButton = document.querySelector('.navstart');
const navMenu = document.querySelector('.nav');

navStartButton.addEventListener('click', () => {
    navMenu.classList.toggle('hidden');
});