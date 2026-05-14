export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx}",
  ],
  theme: {
    extend: {
      colors: {
        'thread': {
          50: '#f9f5f0',
          100: '#f3ebe1',
          200: '#e7d7c3',
          300: '#dbc3a5',
          400: '#cfaf87',
          500: '#c39b69',
          600: '#b78751',
          700: '#ab7339',
          800: '#9f5f21',
          900: '#935609',
        },
        'dark': {
          900: '#0a0a0a',
          800: '#1a1a1a',
          700: '#2d2d2d',
          600: '#404040',
          500: '#535353',
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
      boxShadow: {
        'premium': '0 8px 32px rgba(0, 0, 0, 0.4)',
        'glass': '0 8px 32px 0 rgba(31, 38, 135, 0.37)',
        'thread': '0 20px 60px rgba(195, 155, 105, 0.2)',
      },
      backdropBlur: {
        xs: '2px',
        sm: '4px',
      }
    },
  },
  plugins: [],
}
