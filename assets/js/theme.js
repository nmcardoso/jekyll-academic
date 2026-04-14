(() => {
  'use strict'

  const THEME_KEY = 'theme'

  const getStoredTheme = () => localStorage.getItem(THEME_KEY)

  const setStoredTheme = (theme) => localStorage.setItem(THEME_KEY, theme)

  const getPreferredTheme = () => {
    const stored = getStoredTheme()
    if (stored === 'light' || stored === 'dark') {
      return stored
    }
    return window.matchMedia('(prefers-color-scheme: dark)').matches
      ? 'dark'
      : 'light'
  }

  const setTheme = (theme) => {
    document.documentElement.setAttribute('data-bs-theme', theme)
  }

  const toggleTheme = () => {
    const currentTheme = getPreferredTheme()
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark'
    setStoredTheme(newTheme)
    setTheme(newTheme)
  }

  // Initialize theme on load
  setTheme(getPreferredTheme())

  window.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('theme-switcher')

    if (!button) return

    button.addEventListener('click', toggleTheme)
  })
})()