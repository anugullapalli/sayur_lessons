# Library Book Borrowing App

This is to test a simple single-page application that lets users search, select and borrow books. This is a minimal front-end demo built with HTML, CSS and vanilla JavaScript.

## Features

- Search books by title or author
- Add books to cart
- View total books selected
- Borrowing limit of 5 books (the UI warns when limit reached)
- Remove books from cart
- Optional utility to remove books from inventory via console

## Getting Started

1. **Open locally:**
   - Double-click `index.html` in the `library_app` folder or open it in your browser.
   - No build step or server is required.

2. **Optional server:**
   ```bash
   cd library_app
   python3 -m http.server 8000
   # then browse to http://localhost:8000
   ```

3. **Testing the App:**
   - Enter search terms in the input field, clear with the "Clear" button.
   - Click "Add to Cart" for books; try exceeding the five-book limit.
   - Remove items using the cart's "Remove" buttons.
   - Click "Borrow Books" to complete and reset the cart.
   - From the browser console, run `removeBookFromInventory(id)` to delete an item.

## Files

- `index.html` – main markup
- `style.css` – styling
- `script.js` – application logic

## License

MIT
