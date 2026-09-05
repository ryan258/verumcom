/** VERUM: progressively enhanced navigation and collection filters. */
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

  const filterBar = document.querySelector('.filter-bar');
  const cards = [...document.querySelectorAll('.piece-card[data-categories]')];
  if (!filterBar || !cards.length) return;
  const buttons = [...filterBar.querySelectorAll('[data-filter-type]')];
  const count = document.getElementById('filter-count');
  const empty = document.querySelector('.filter-empty');
  const reset = document.querySelector('.filter-reset');
  const selected = { category: 'all', drop: 'all' };
  const valid = (key, value) => buttons.some(button => button.dataset.filterType === key && button.dataset.filterVal === value);
  const render = (isInitial = false) => {
    let visible = 0;
    cards.forEach(card => {
      const categories = (card.dataset.categories || '').split(',');
      card.hidden = !((selected.category === 'all' || categories.includes(selected.category)) &&
        (selected.drop === 'all' || card.dataset.drop === selected.drop));
      if (!card.hidden) visible += 1;
    });
    buttons.forEach(button => button.setAttribute('aria-pressed', String(selected[button.dataset.filterType] === button.dataset.filterVal)));
    if (count) {
      count.textContent = `${visible} / ${cards.length} ${count.dataset.label}`;
      if (!isInitial) count.setAttribute('aria-live', 'polite');
    }
    if (empty) empty.hidden = visible !== 0;
    if (reset) {
      reset.hidden = false;
      reset.disabled = selected.category === 'all' && selected.drop === 'all';
    }
  };
  const readURL = (isInitial = false) => {
    const params = new URLSearchParams(window.location.search);
    for (const key of Object.keys(selected)) {
      const value = params.get(key);
      selected[key] = valid(key, value) ? value : 'all';
    }
    render(isInitial && selected.category === 'all' && selected.drop === 'all');
  };
  const saveURL = () => {
    const url = new URL(window.location.href);
    for (const [key, value] of Object.entries(selected)) {
      if (value === 'all') url.searchParams.delete(key);
      else url.searchParams.set(key, value);
    }
    // Filters still work in environments that restrict history writes.
    try { window.history.replaceState(null, '', url); } catch { /* Keep local state. */ }
  };
  buttons.forEach(button => button.addEventListener('click', () => {
    selected[button.dataset.filterType] = button.dataset.filterVal;
    render();
    saveURL();
  }));
  reset.addEventListener('click', () => {
    selected.category = selected.drop = 'all';
    render();
    saveURL();
    buttons[0].focus();
  });
  window.addEventListener('popstate', () => readURL(false));
  filterBar.hidden = false;
  readURL(true);
});
