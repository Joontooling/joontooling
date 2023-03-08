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

// 마우스 올렸을 때 나타나는 버튼들
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

// 버튼 클릭시 슬라이드 회전하기
let counter = 0;
let bigSlideSize = 494;
let smallSlideSize = 111;

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

  thumbnailSwiperLis.forEach((slide, idx) => {
    slide.classList.remove('swiper-slide-active');
    let slideActiveIdx = document
      .querySelector('.swiper-slide-active')
      .getAttribute('data-swiper-slide-index');

    if (Number(slideActiveIdx) === idx) {
      thumbnailSwiperLis[idx].classList.add('swiper-slide-active');
    }
    slide.style.transform = `translateX(-${counter * smallSlideSize}px)`;
  });
}

// 썸네일 클릭시 슬라이드 회전하기
thumbnailSwiperLis.forEach((li, idx) => {
  li.addEventListener('click', () => {
    bigSlideStyleChange(idx);
    liStyleChange(li);
    moveSlide(idx);
  });
});

function bigSlideStyleChange(idx) {
  productSwiperUl.style.transform = `translate3d(${
    -bigSlideSize * idx
  }px, 0px, 0px)`;
}

function liStyleChange(li) {
  thumbnailSwiperLis.forEach((item) => {
    item.classList.remove('swiper-slide-active');
  });
  li.classList.add('swiper-slide-active');
}

function moveSlide(idx) {
  thumbnailSwiperLis.forEach((li) => {
    li.style.transform = `translateX(-${idx * smallSlideSize}px)`;
  });
}
