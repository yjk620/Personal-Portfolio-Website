document.addEventListener('DOMContentLoaded', function () {
  let mouseCursor = document.querySelector('.cursor');
  let navLinks = document.querySelectorAll('.nav-links li');
  let hyperlink = document.querySelectorAll('.boxContact a');

  window.addEventListener('mousemove', cursor);

  function cursor(e) {
    mouseCursor.style.top = e.pageY - scrollY + 'px';
    mouseCursor.style.left = e.pageX + 'px';
  }

  navLinks.forEach((link) => {
    link.addEventListener('mouseleave', () => {
      mouseCursor.classList.remove('link-grow');
    });
    link.addEventListener('mouseover', () => {
      mouseCursor.classList.add('link-grow');
    });
  });
});
