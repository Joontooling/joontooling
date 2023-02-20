const header = document.querySelector('.header');
const headerHeight = header.offsetHeight;
const navHeight = 70;

const navi = document.querySelector('.nav');
const naviWrapper = navi.querySelector('.nav-wrapper');
const innerMenu = navi.querySelector('.inner__menu');

const categoryMenuIcon = document.querySelector('.inner__menu__icon');
const category = document.querySelector('.category__wrap');

window.addEventListener('scroll', () => {
  let scrollLocation = document.documentElement.scrollTop;
  if (scrollLocation > headerHeight - navHeight) {
    showNavigation('none');
    header.classList.add('header--fixed');
  } else {
    showNavigation('block');
    header.classList.remove('header--fixed');
  }
});
function showNavigation(display) {
  naviWrapper.style.display = display;
  innerMenu.style.display = display;
}

categoryMenuIcon.addEventListener('click', () => {
  category.classList.toggle('active');
  if (category.classList.contains('active')) {
    categoryIconStyleToggle('black', 'white');
    categoryMenuIcon.querySelector('i').classList.add('fa-x');
  } else {
    categoryIconStyleToggle('white', 'black');
    categoryMenuIcon.querySelector('i').classList.remove('fa-x');
  }
});
function categoryIconStyleToggle(backColor, fontColor) {
  categoryMenuIcon.style.background = backColor;
  categoryMenuIcon.style.color = fontColor;
}
