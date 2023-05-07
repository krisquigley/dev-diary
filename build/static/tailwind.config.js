/** @type {import('tailwindcss/types').Config} */
module.exports = {
  content: [
    '../templates/**/*.html.j2',
    './src/**/*.js',
    './node_modules/flowbite/**/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [require('flowbite/plugin')],
};
