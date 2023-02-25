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
const productSwiperUl = document.querySelector(
  '.productSwiper .swiper-wrapper'
);
const productSwiperLis = document.querySelectorAll(
  '.productSwiper .swiper-wrapper .swiper-slide'
);
const thumbnailSwiper = document.querySelector('.thumbnailSwiper');
const thumbnailSwiperUl = document.querySelector(
  '.thumbnailSwiper .swiper-wrapper'
);
const thumbnailSwiperLis = document.querySelectorAll(
  '.thumbnailSwiper .swiper-wrapper .swiper-slide'
);
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
