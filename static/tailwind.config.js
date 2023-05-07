/** @type {import('tailwindcss/types').Config} */
const colors = require('tailwindcss/colors');

module.exports = {
  content: [
    '../templates/**/*.html',
    './src/**/*.js',
    './node_modules/flowbite/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        primary: colors.violet,
      },
    },
  },
  plugins: [require('flowbite/plugin')],
};
