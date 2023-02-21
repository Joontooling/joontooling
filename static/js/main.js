// Header
const header = document.querySelector('.header');
const headerHeight = header.offsetHeight;
const main = document.querySelector('main');

// Navigation
const navi = document.querySelector('.nav');
const naviWrapper = navi.querySelector('.nav-wrapper');
const innerMenu = navi.querySelector('.inner__menu');
const navHeight =
  navi.offsetHeight -
  innerMenu.offsetHeight -
  naviWrapper.querySelector('.nav__items').offsetHeight;

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

// event product swiper
let ProductSwiper = new Swiper('.productSwiper', {
  slidesPerView: 1,
  spaceBetween: 30,
  loop: true,
  navigation: {
    prevEl: '.swiper-button-prev',
    nextEl: '.swiper-button-next',
  },
});
let swiper = new Swiper('.thumbnailSwiper', {
  slidesPerView: 4,
  spaceBetween: 10,
  centeredSlides: true,
});

// product swiper mouse event
const productSwiper = document.querySelector('.productSwiper');
const productSwiperUl = productSwiper.querySelector('.swiper-wrapper');
const productSwiperLis = productSwiperUl.querySelectorAll('.swiper-slide');
const thumbnailSwiper = document.querySelector('.thumbnailSwiper');
const thumbnailSwiperUl = thumbnailSwiper.querySelector('.swiper-wrapper');
const thumbnailSwiperLis = thumbnailSwiperUl.querySelectorAll('.swiper-slide');
const prevBtn = document.querySelector('.prevBtn');
const nextBtn = document.querySelector('.nextBtn');

productSwiper.addEventListener('mouseover', () => {
  let buttons = productSwiper.querySelectorAll('button');
  productSwiperBtnsHover(buttons, 1);
});
productSwiper.addEventListener('mouseout', () => {
  let buttons = productSwiper.querySelectorAll('button');
  productSwiperBtnsHover(buttons, 0);
});
function productSwiperBtnsHover(btns, opacity) {
  btns.forEach((button) => {
    button.style.opacity = opacity;
  });
}

let counter = 0;

nextBtn.addEventListener('click', () => {
  counter++;
  carousel();
});
prevBtn.addEventListener('click', () => {
  counter--;
  carousel();
});

function carousel() {
  if (counter === thumbnailSwiperLis.length) {
    counter = 0;
  }
  if (counter < 0) {
    counter = thumbnailSwiperLis.length - 1;
  }
  thumbnailSwiperLis.forEach((slide) => {
    slide.style.transform = `translateX(-${counter * 111}px)`;
  });
}
