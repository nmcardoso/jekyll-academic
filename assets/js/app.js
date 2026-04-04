/**
 * Copia uma string para a área de transferência.
 * Tenta usar a API moderna navigator.clipboard.writeText.
 * Se falhar ou não estiver disponível, usa o método antigo (execCommand) como fallback.
 *
 * @param {string} text - A string a ser copiada.
 * @returns {Promise<void>} Uma Promise que resolve quando a cópia for bem-sucedida ou rejeita em caso de erro.
 */
function copyToClipboard(text) {
  if (navigator.clipboard && window.isSecureContext) {
    return navigator.clipboard.writeText(text).catch(() => {
      return copyToClipboardFallback(text);
    });
  } else {
    return copyToClipboardFallback(text);
  }
}

/**
 * Implementação do fallback usando document.execCommand('copy').
 * Cria um elemento <textarea> temporário, seleciona o texto e executa o comando.
 *
 * @param {string} texto - Texto a ser copiado.
 * @returns {Promise<void>}
 */
function copyToClipboardFallback(texto) {
  return new Promise((resolve, reject) => {
    const textarea = document.createElement('textarea');
    textarea.value = texto;
    textarea.style.position = 'fixed';   // Evita rolagem da página
    textarea.style.opacity = '0';        // Invisível
    textarea.style.left = '-999px';
    textarea.style.top = '0';
    document.body.appendChild(textarea);

    textarea.focus();
    textarea.select();

    try {
      const sucesso = document.execCommand('copy');
      if (sucesso) {
        resolve();
      } else {
        reject(new Error('Falha ao copiar usando o método antigo.'));
      }
    } catch (erro) {
      reject(erro);
    } finally {
      document.body.removeChild(textarea);
    }
  });
}


function copyString(text, successMessage, errorMessage) {
  return copyToClipboard(text)
    .then(() => {
      if (successMessage) {
        Toastify({
          text: successMessage,
          duration: 2500,
          close: true,
          gravity: "bottom", // `top` or `bottom`
          position: "right", // `left`, `center` or `right`
          stopOnFocus: true, // Prevents dismissing of toast on hover
          className: "bg-primary"
        }).showToast()
      }
    })
    .catch(() => {
      if (errorMessage) {
        Toastify({
          text: errorMessage,
          duration: 3000,
          close: true,
          gravity: "bottom", // `top` or `bottom`
          position: "right", // `left`, `center` or `right`
          stopOnFocus: true, // Prevents dismissing of toast on hover
          className: "bg-danger"
        }).showToast()
      }
    })
}

function setupCopyToClipboardButton() {
  document.querySelectorAll('[data-copy-element]').forEach(e => {
    e.addEventListener('click', () => {
      const valEl = document.querySelector(e.dataset.copyElement)
      if (!!valEl) {
        copyString(valEl.textContent.trim(), e.dataset?.success, e.dataset?.error)
      }
    })
  })

  document.querySelectorAll('[data-copy-text]').forEach(e => {
    e.addEventListener('click', () => {
      copyString(e.copyText, e.dataset?.success, e.dataset?.error)
    })
  })
}

function setupPopovers() {
  const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
  const popoverList = [...popoverTriggerList].map(triggerEl => new bootstrap.Popover(triggerEl, {html: true}))
}

function setupTooltips() {
  const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
  const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))
}

function setupModals() {
  const modalTriggerList = document.querySelectorAll('[data-bs-toggle="modal"]')
  const modalList = [...modalTriggerList].map(triggerEl => {
    const modalEl = document.querySelector(triggerEl.getAttribute('data-bs-target'))
    if (!!modalEl) {
      modalEl.addEventListener('shown.bs.modal', () => {
        triggerEl.focus()
      })
    }
  })
}

function setupTables() {
  const article = document.querySelector('article#post-content')
  if (!!article) {
    article.querySelectorAll('table').forEach(table => {
      // add classes bootstrap classes to the table
      table.classList.add('table', 'table-hover')

      const caption = table.querySelector('caption')
      if (!!caption && !caption.firstChild.textContent.toLowerCase().startsWith('note')) {
        caption.classList.add('text-secondary-emphasis', 'text-justify')
        const span = document.createElement('span')
        span.classList.add('text-sc')
        span.innerHTML = 'Notes &mdash; '
        caption.insertBefore(span, caption.firstChild)
      }

      // wrap table inside div (for small devices)
      const wrapper = document.createElement('div')
      table.parentNode.insertBefore(wrapper, table)
      wrapper.appendChild(table)
      wrapper.classList.add('table-wrapper')
    })
  }
}

function setupCodeHighlight() {
  // https://remarkablemark.org/blog/2021/06/01/add-copy-code-to-clipboard-button-to-jeyll-site/
  const codeBlocks = document.querySelectorAll('.highlight > pre')

  codeBlocks.forEach(function (codeBlock) {
    const copyButton = document.createElement('button')
    const copyHtml = '<i class="far fa-copy fa-sm me-1"></i>Copy'

    copyButton.className = 'btn btn-light'
    copyButton.type = 'button'
    copyButton.ariaLabel = 'Copy code to clipboard'
    copyButton.innerHTML = copyHtml

    codeBlock.append(copyButton)

    copyButton.addEventListener('click', function () {
      const code = codeBlock.querySelector('code').innerText.trim()
      window.navigator.clipboard.writeText(code)

      copyButton.innerHTML = '<i class="fas fa-check fa-xs me-1 text-success"></i>Copied'
      const timeout = 3500

      setTimeout(function () {
        copyButton.innerHTML = copyHtml
        copyButton.blur()
      }, timeout)
    })
  })
}


function init() {
  // setupCopyToClipboardButton()
  setupPopovers()
  setupTooltips()
  setupModals()
  setupTables()
  setupCodeHighlight()
}

window.addEventListener('load', init)
