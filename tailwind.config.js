/** @type {import('tailwindcss/types').Config} */
const colors = require('tailwindcss/colors');

module.exports = {
  darkMode: 'class',
  content: ['./templates/**/*.html', './static/**/*.js'],
  theme: {
    extend: {
      colors: {
        primary: colors.violet,
      },
    },
  },
  plugins: [require('flowbite/plugin')],
};
