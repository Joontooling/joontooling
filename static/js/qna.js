// QnA image preview (single)
// function readURL(input) {
//   if (input.files && input.files[0]) {
//     let reader = new FileReader();
//     let previewImg = document.querySelector('#preview');
//     reader.onload = (e) => {
//       previewImg.src = e.target.result;
//       previewImg.style.display = 'block';
//     };
//     reader.readAsDataURL(input.files[0]);
//   } else {
//     previewImg.src = '';
//     previewImg.style.display = 'none';
//   }
// }

// QnA image preview (multiple)
function imageChange(input) {
  let i = input.files.length - 1;

  for (let image of input.files) {
    let imgTag = document.createElement('img');
    const reader = new FileReader();
    reader.onload = function (e) {
      imgTag.setAttribute('src', e.target.result);
      imgTag.classList.add('preview');
    };
    reader.readAsDataURL(input.files[i--]);
    document.querySelector('.preview-container').appendChild(imgTag);
  }
}
