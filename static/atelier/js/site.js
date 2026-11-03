(() => {
  const menuButton = document.querySelector('.menu-toggle');
  const navigation = document.querySelector('#primary-nav');
  if (menuButton && navigation) {
    menuButton.addEventListener('click', () => {
      const open = menuButton.getAttribute('aria-expanded') !== 'true';
      menuButton.setAttribute('aria-expanded', String(open));
      navigation.classList.toggle('is-open', open);
    });
    navigation.addEventListener('click', (event) => {
      if (event.target.closest('a')) {
        menuButton.setAttribute('aria-expanded', 'false');
        navigation.classList.remove('is-open');
      }
    });
  }

  const lightbox = document.querySelector('.lightbox');
  if (lightbox) {
    const image = lightbox.querySelector('img');
    const caption = lightbox.querySelector('p');
    const close = lightbox.querySelector('.lightbox-close');
    document.querySelectorAll('[data-lightbox]').forEach((trigger) => {
      trigger.addEventListener('click', () => {
        const source = trigger.querySelector('img');
        image.src = source.src;
        image.alt = source.alt;
        caption.textContent = trigger.dataset.caption || '';
        lightbox.showModal();
      });
    });
    close.addEventListener('click', () => lightbox.close());
    lightbox.addEventListener('click', (event) => {
      if (event.target === lightbox) lightbox.close();
    });
  }
})();
