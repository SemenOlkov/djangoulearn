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

document.getElementById('2to1').addEventListener('click', function() {
    document.getElementById('2').classList.add('hidden');
    document.getElementById('1').classList.remove('hidden');
});
document.getElementById('1to2').addEventListener('click', function() {
    document.getElementById('1').classList.add('hidden');
    document.getElementById('2').classList.remove('hidden');
});
document.getElementById('3to2').addEventListener('click', function() {
    document.getElementById('3').classList.add('hidden');
    document.getElementById('2').classList.remove('hidden');
});
document.getElementById('2to3').addEventListener('click', function() {
    document.getElementById('2').classList.add('hidden');
    document.getElementById('3').classList.remove('hidden');
});
document.getElementById('4to3').addEventListener('click', function() {
    document.getElementById('4').classList.add('hidden');
    document.getElementById('3').classList.remove('hidden');
});
document.getElementById('3to4').addEventListener('click', function() {
    document.getElementById('3').classList.add('hidden');
    document.getElementById('4').classList.remove('hidden');
});
document.getElementById('5to4').addEventListener('click', function() {
    document.getElementById('5').classList.add('hidden');
    document.getElementById('4').classList.remove('hidden');
});
document.getElementById('4to5').addEventListener('click', function() {
    document.getElementById('4').classList.add('hidden');
    document.getElementById('5').classList.remove('hidden');
});
document.getElementById('5to6').addEventListener('click', function() {
    document.getElementById('5').classList.add('hidden');
    document.getElementById('6').classList.remove('hidden');
});
document.getElementById('6to5').addEventListener('click', function() {
    document.getElementById('6').classList.add('hidden');
    document.getElementById('5').classList.remove('hidden');
});
document.getElementById('6to7').addEventListener('click', function() {
    document.getElementById('6').classList.add('hidden');
    document.getElementById('7').classList.remove('hidden');
});
document.getElementById('7to6').addEventListener('click', function() {
    document.getElementById('7').classList.add('hidden');
    document.getElementById('6').classList.remove('hidden');
});
document.getElementById('7to8').addEventListener('click', function() {
    document.getElementById('7').classList.add('hidden');
    document.getElementById('8').classList.remove('hidden');
});
document.getElementById('8to7').addEventListener('click', function() {
    document.getElementById('8').classList.add('hidden');
    document.getElementById('7').classList.remove('hidden');
});
document.getElementById('8to9').addEventListener('click', function() {
    document.getElementById('8').classList.add('hidden');
    document.getElementById('9').classList.remove('hidden');
});
document.getElementById('9to8').addEventListener('click', function() {
    document.getElementById('9').classList.add('hidden');
    document.getElementById('8').classList.remove('hidden');
});
document.getElementById('9to10').addEventListener('click', function() {
    document.getElementById('9').classList.add('hidden');
    document.getElementById('10').classList.remove('hidden');
});
document.getElementById('10to9').addEventListener('click', function() {
    document.getElementById('10').classList.add('hidden');
    document.getElementById('9').classList.remove('hidden');
});

