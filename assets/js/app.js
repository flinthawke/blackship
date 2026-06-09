document.addEventListener('DOMContentLoaded', () => {
  const externalLinks = document.querySelectorAll('a[target="_blank"]');
  externalLinks.forEach((link) => {
    link.addEventListener('click', () => {
      console.log('affiliate click:', link.href);
    });
  });
});
