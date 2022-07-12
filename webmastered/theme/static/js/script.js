function isNavbarOverDarkContent() {
    var navbarOffset = $(".wm-navigation").offset().top;
    var heroOffset = $(".wm-hero-container").offset().top;
    var heroHeight = $(".wm-hero-container").outerHeight(true);
    var darkContainersOnScreen = document.getElementsByClassName('wm-container-dark-onscreen');
    if (darkContainersOnScreen.length > 0) {
        var alternateOffset = $(".wm-container-dark-onscreen").offset().top;
        var alternateHeight = $(".wm-container-dark-onscreen").outerHeight(true);
        if (navbarOffset >= heroOffset && navbarOffset <= heroHeight) {
            return true
        } else {
            if (navbarOffset >= alternateOffset && navbarOffset <= (alternateHeight + alternateOffset)) {
                return true
            } else {
                return false
            }
        }
    } else {
        if (navbarOffset >= heroOffset && navbarOffset <= heroHeight) {
            return true
        } else {
            return false
        }
    }
}

let isNavbarInDarkMode = null;
jQuery(document).ready(function() {
  window.addEventListener('scroll', function(e) {
    let wm_header_logo_container = document.querySelector('.wm-navigation')
    if (isNavbarOverDarkContent()) {
      if (isNavbarInDarkMode == false || isNavbarInDarkMode == null) {
        wm_header_logo_container._x_dataStack[0].navbarOverDarkContent = true;
        isNavbarInDarkMode = true;
      }
    } else {
      if (isNavbarInDarkMode == true || isNavbarInDarkMode == null) {
        wm_header_logo_container._x_dataStack[0].navbarOverDarkContent = false;
        isNavbarInDarkMode = false
      }
    }
  });
});
