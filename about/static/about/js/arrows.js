document.addEventListener('DOMContentLoaded', function() {
  const sections = document.querySelectorAll('.section');
  let currentSectionIndex = 0;

  function showCurrentSection() {
    sections.forEach((section, index) => {
      if (index === currentSectionIndex) {
        section.style.display = 'block';
      } else {
        section.style.display = 'none';
      }
    });
  }

  showCurrentSection();

  document.querySelector('.prev-section').addEventListener('click', function() {
    currentSectionIndex = Math.max(0, currentSectionIndex - 1);
    showCurrentSection();
  });

  document.querySelector('.next-section').addEventListener('click', function() {
    currentSectionIndex = Math.min(sections.length - 1, currentSectionIndex + 1);
    showCurrentSection();
  });

  document.addEventListener('keydown', function(event) {
    if (event.key === 'ArrowLeft') {
      currentSectionIndex = Math.max(0, currentSectionIndex - 1);
      showCurrentSection();
    } else if (event.key === 'ArrowRight') {
      currentSectionIndex = Math.min(sections.length - 1, currentSectionIndex + 1);
      showCurrentSection();
    }
  });
});
