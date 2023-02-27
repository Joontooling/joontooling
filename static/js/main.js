'use strict';

// Header
const header = document.querySelector('.header');
const headerHeight = header.offsetHeight;
const main = document.querySelector('#main');

// Navigation
const navi = document.querySelector('.navi');
const naviWrapper = navi.querySelector('.nav-wrapper');
const innerMenu = navi.querySelector('.inner__menu');
const navHeight =
  navi.offsetHeight -
  innerMenu.offsetHeight -
  naviWrapper.querySelector('.nav__items').offsetHeight +
  3;

// Category
const categoryMenuIcon = document.querySelector('.inner__menu__icon');
const category = document.querySelector('.category__wrap');
const categoryMenuIcons = document.querySelectorAll('.inner__menu__icon');

// Events
// event scroll
window.addEventListener('scroll', () => {
  let scrollLocation = document.documentElement.scrollTop;
  if (scrollLocation > headerHeight - navHeight) {
    showNavigation('none');
    header.classList.add('header--fixed');
    main.style.paddingTop = `${headerHeight}px`;
  } else {
    showNavigation('block');
    header.classList.remove('header--fixed');
    main.style.removeProperty('padding');
  }
});
function showNavigation(display) {
  naviWrapper.style.display = display;
  innerMenu.style.display = display;
}

// event category
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
