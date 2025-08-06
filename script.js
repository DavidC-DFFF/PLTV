// 🎨 Thème clair/sombre avec mémorisation
function setupThemeToggle() {
  const toggleButton = document.getElementById('toggle-theme');
  if (toggleButton) {
    toggleButton.addEventListener('click', () => {
      const currentTheme = document.documentElement.dataset.theme;
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      document.documentElement.dataset.theme = newTheme;
      localStorage.setItem('theme', newTheme);
    });
  }

  const savedTheme = localStorage.getItem('theme') || 'light';
  document.documentElement.dataset.theme = savedTheme;
}

// 📖 Redirection via la table des matières
function goToChapter(selectElement) {
  const page = selectElement.value;
  if (!page) return;

  const currentPath = window.location.pathname;
  const isInCapitoli = currentPath.includes('/capitoli/');
  const base = isInCapitoli ? '' : 'capitoli/';
  const fullPath = page.startsWith('capitolo') ? base + page : page;

  localStorage.setItem('lastPage', fullPath);
  window.location.href = fullPath;
}

// 📌 Mémoriser la page actuelle (sauf index.html)
window.addEventListener('beforeunload', () => {
  const fullPath = window.location.pathname;
  const match = fullPath.match(/\/PLTV\/(capitoli\/capitolo\d+\.html)/);
  if (match) {
    localStorage.setItem('lastPage', match[1]);
  }
});

// 🔗 Intercepter les clics sur le lien "Sommaire"
function setupSommaireInterception() {
  const sommaireBtn = document.querySelector('a.nav-left[href="../index.html"], a.nav-left[href="index.html"]');
  if (sommaireBtn) {
    sommaireBtn.addEventListener('click', () => {
      sessionStorage.setItem('manualIndex', 'true');
    });
  }
}

// 📥 Charger dynamiquement navbar.html
function loadNavbar() {
  const navbarContainer = document.getElementById('navbar');
  if (navbarContainer) {
    const base = window.location.pathname.includes('/capitoli/') ? '../' : './';
    fetch(base + 'navbar.html')
      .then(response => response.text())
      .then(html => {
        navbarContainer.innerHTML = `
          <nav class="navbar">
            <div class="navbar-inner">
              ${html}
            </div>
          </nav>
        `;
        setupThemeToggle();
        setupSommaireInterception();
        selectCurrentChapter();
        setupFontSizeToggle();
      });
  } else {
    setupThemeToggle();
    setupSommaireInterception();
  }
}

// ✅ Marquer automatiquement le chapitre actif dans le menu TOC
function selectCurrentChapter() {
  const toc = document.getElementById('toc');
  if (toc) {
    const current = window.location.pathname.split('/').pop();
    for (let option of toc.options) {
      if (option.value === current) {
        option.selected = true;
        break;
      }
    }
  }
}

// 📊 Barre de progression globale
function updateGlobalProgressBar() {
  const chapterOrder = [
    'index.html',
    'capitolo01.html',
    'capitolo02.html',
    'capitolo03.html',
    'capitolo04.html',
    'capitolo05.html',
    'capitolo06.html',
    'capitolo07.html',
    'capitolo08.html',
    'capitolo09.html',
    'capitolo10.html',
    'capitolo11.html',
    'capitolo12.html',
    'capitolo13.html',
    'capitolo14.html',
    'capitolo15.html',
    'capitolo16.html',
    'capitolo17.html',
    'capitolo18.html',
    'capitolo19.html',
    'capitolo20.html',
    'capitolo21.html',
    'capitolo22.html',
    'capitolo23.html',
    'capitolo24.html',
    'capitolo25.html',
    'capitolo26.html',
    'capitolo27.html',
    'capitolo28.html',
    'capitolo29.html',
    'capitolo30.html',
    'capitolo31.html',
    'capitolo32.html',
    'capitolo33.html',
    'capitolo34.html',
    'capitolo35.html',
    'capitolo36.html',
    'capitolo37.html',
    'capitolo38.html',
    'capitolo39.html',
    'capitolo40.html',
    'capitolo41.html',
    'capitolo42.html',
    'capitolo43.html',
    'capitolo44.html',
    'capitolo45.html',
    'capitolo46.html',
    'capitolo47.html',
    'capitolo48.html',
    'capitolo49.html',
    'capitolo50.html',
    'capitolo51.html',
    'capitolo52.html',
    'capitolo53.html',
    'capitolo54.html',
    'capitolo55.html',
    'capitolo56.html',
    'capitolo57.html',
    'capitolo58.html',
    'capitolo59.html',
    'fine.html'
  ];

  const currentPath = window.location.pathname.split('/').pop();
  const index = chapterOrder.indexOf(currentPath);

  if (index !== -1) {
    const progressPercent = ((index + 1) / chapterOrder.length) * 100;
    const bar = document.getElementById('global-progress');
    if (bar) bar.style.width = progressPercent + '%';
  }
}

// ▶️ Initialisation au chargement
window.addEventListener('DOMContentLoaded', () => {
  loadNavbar();
  setupFontSizeToggle();
  updateGlobalProgressBar();
});

function setupFontSizeToggle() {
  const button = document.getElementById('toggle-font');
  const sizes = ['small', 'medium', 'large'];
  let current = localStorage.getItem('fontSize') || 'medium';

  const applySize = (size) => {
    document.documentElement.dataset.font = size;
    localStorage.setItem('fontSize', size);
  };

  applySize(current);

  if (button) {
    button.addEventListener('click', () => {
      const index = (sizes.indexOf(current) + 1) % sizes.length;
      current = sizes[index];
      applySize(current);
    });
  }
}
