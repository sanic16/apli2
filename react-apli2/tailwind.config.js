/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './src/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      'hero-pattern': "url('https://important-archives-jsanic16.s3.amazonaws.com/css_projects/blog/jorge-ramirez-anT-7GmycsY-unsplash.jpg')"
    },
  },
  plugins: [],
}

