/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}',"./node_modules/flowbite/**/*.js"], // specify the paths to your pages and components
    // darkMode: false,
    theme: {
        extend: {},
    },
    plugins: [
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/line-clamp'),
        require('flowbite/plugin')
    ],
}