const navStartButton = document.querySelector('.navstart');
const navMenu = document.querySelector('.nav');

navStartButton.addEventListener('click', () => {
    navMenu.classList.toggle('hidden');
});

document.getElementById("mainButton").addEventListener('click',() => {
    window.location.href = '/'
});

document.getElementById("aboutButton").addEventListener('click',() => {
    window.location.hash = '#footer';
});
