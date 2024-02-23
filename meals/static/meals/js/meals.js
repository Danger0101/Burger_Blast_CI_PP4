function showCategory(category) {
    var categories = document.querySelectorAll(".menu-category");
    categories.forEach(function (cat) {
      if (cat.id === category) {
        cat.style.display = "block";
      } else {
        cat.style.display = "none";
      }
    });
  }