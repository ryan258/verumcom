/**
 * VERUM — Minimal Accessible UI Engine
 * Vanilla JS under 4KB, 0 dependencies
 */
document.addEventListener('DOMContentLoaded', () => {
  // Mobile Navigation Drawer Toggle
  const toggleBtn = document.querySelector('.site-header__toggle');
  const navMenu = document.querySelector('.main-nav');

  if (toggleBtn && navMenu) {
    toggleBtn.addEventListener('click', () => {
      const isExpanded = toggleBtn.getAttribute('aria-expanded') === 'true';
      toggleBtn.setAttribute('aria-expanded', !isExpanded);
      navMenu.classList.toggle('main-nav--open');
      document.body.classList.toggle('u-no-scroll', !isExpanded);
    });

    // Close on ESC
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && navMenu.classList.contains('main-nav--open')) {
        toggleBtn.setAttribute('aria-expanded', 'false');
        navMenu.classList.remove('main-nav--open');
        document.body.classList.remove('u-no-scroll');
        toggleBtn.focus();
      }
    });
  }

  // Lookbook Interactive Filter (Progressive Enhancement)
  const filterBtns = document.querySelectorAll('.filter-bar__btn');
  const pieceCards = document.querySelectorAll('.piece-card');

  if (filterBtns.length > 0 && pieceCards.length > 0) {
    filterBtns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const filterType = btn.dataset.filterType; // 'all', 'category', 'drop'
        const filterVal = btn.dataset.filterVal;

        // Update active class within group
        const group = btn.closest('.filter-bar__group');
        if (group) {
          group.querySelectorAll('.filter-bar__btn').forEach(b => b.classList.remove('filter-bar__btn--active'));
          btn.classList.add('filter-bar__btn--active');
        }

        pieceCards.forEach(card => {
          if (filterType === 'all' || filterVal === 'all') {
            card.style.display = 'flex';
          } else if (filterType === 'category') {
            const categories = card.dataset.categories ? card.dataset.categories.split(',') : [];
            card.style.display = categories.includes(filterVal) ? 'flex' : 'none';
          } else if (filterType === 'drop') {
            const drop = card.dataset.drop;
            card.style.display = (drop === filterVal) ? 'flex' : 'none';
          }
        });
      });
    });
  }
});
