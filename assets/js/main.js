/** VERUM: progressively enhanced navigation. */
document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.site-header__toggle');
  const navigation = document.querySelector('.main-nav');
  if (toggle && navigation) {
    const mobile = window.matchMedia('(max-width: 900px)');
    const setOpen = (open, restoreFocus = false) => {
      toggle.setAttribute('aria-expanded', String(open));
      navigation.hidden = mobile.matches && !open;
      if (restoreFocus) toggle.focus();
    };
    const syncLayout = () => {
      const focusWasInNav = navigation.contains(document.activeElement);
      toggle.hidden = !mobile.matches;
      setOpen(false, mobile.matches && focusWasInNav);
    };
    toggle.addEventListener('click', () => setOpen(toggle.getAttribute('aria-expanded') !== 'true'));
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && mobile.matches && toggle.getAttribute('aria-expanded') === 'true') {
        setOpen(false, true);
      }
    });
    // This is an inline disclosure: the rest of the document stays reachable.
    document.addEventListener('click', event => {
      if (mobile.matches && !event.target.closest('.site-header')) setOpen(false);
    });
    navigation.addEventListener('click', event => {
      if (mobile.matches && event.target.closest('a')) setOpen(false, true);
    });
    mobile.addEventListener('change', syncLayout);
    syncLayout();
  }

});
