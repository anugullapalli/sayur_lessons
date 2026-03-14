// Sample Book Database
const books = [
    { id: 1, title: "To Kill a Mockingbird", author: "Harper Lee", year: 1960 },
    { id: 2, title: "1984", author: "George Orwell", year: 1949 },
    { id: 3, title: "Pride and Prejudice", author: "Jane Austen", year: 1813 },
    { id: 4, title: "The Great Gatsby", author: "F. Scott Fitzgerald", year: 1925 },
    { id: 5, title: "Jane Eyre", author: "Charlotte Brontë", year: 1847 },
    { id: 6, title: "Wuthering Heights", author: "Emily Brontë", year: 1847 },
    { id: 7, title: "Moby Dick", author: "Herman Melville", year: 1851 },
    { id: 8, title: "The Odyssey", author: "Homer", year: -800 },
    { id: 9, title: "Crime and Punishment", author: "Fyodor Dostoevsky", year: 1866 },
    { id: 10, title: "The Brothers Karamazov", author: "Fyodor Dostoevsky", year: 1879 },
    { id: 11, title: "Anna Karenina", author: "Leo Tolstoy", year: 1877 },
    { id: 12, title: "War and Peace", author: "Leo Tolstoy", year: 1869 },
    { id: 13, title: "The Catcher in the Rye", author: "J.D. Salinger", year: 1951 },
    { id: 14, title: "Lord of the Flies", author: "William Golding", year: 1954 },
    { id: 15, title: "Brave New World", author: "Aldous Huxley", year: 1932 },
    { id: 16, title: "The Hobbit", author: "J.R.R. Tolkien", year: 1937 },
    { id: 17, title: "Fahrenheit 451", author: "Ray Bradbury", year: 1953 },
];

// Application State
const appState = {
    borrowingLimit: 5,
    cart: [],
    filteredBooks: [...books],
};

// DOM Elements
const booksGrid = document.getElementById('booksGrid');
const cartItems = document.getElementById('cartItems');
const searchInput = document.getElementById('searchInput');
const clearSearchBtn = document.getElementById('clearSearchBtn');
const checkoutBtn = document.getElementById('checkoutBtn');
const totalBorrowedEl = document.getElementById('totalBorrowed');
const remainingEl = document.getElementById('remaining');
const cartTotalEl = document.getElementById('cartTotal');

// Initialize App
function init() {
    renderBooks(appState.filteredBooks);
    setupEventListeners();
    updateStats();
}

// Setup Event Listeners
function setupEventListeners() {
    searchInput.addEventListener('input', handleSearch);
    clearSearchBtn.addEventListener('click', handleClearSearch);
    checkoutBtn.addEventListener('click', handleCheckout);
    
    // Modal event listeners
    document.getElementById('closeModal').addEventListener('click', closeBookModal);
    window.addEventListener('click', (e) => {
        const modal = document.getElementById('bookModal');
        if (e.target === modal) {
            closeBookModal();
        }
    });
}

// Handle Search
function handleSearch(e) {
    const searchTerm = e.target.value.toLowerCase();
    appState.filteredBooks = books.filter(book =>
        book.title.toLowerCase().includes(searchTerm) ||
        book.author.toLowerCase().includes(searchTerm)
    );
    renderBooks(appState.filteredBooks);
}

// Handle Clear Search
function handleClearSearch() {
    searchInput.value = '';
    appState.filteredBooks = [...books];
    renderBooks(appState.filteredBooks);
}

// Render Books
function renderBooks(booksToRender) {
    booksGrid.innerHTML = '';
    
    if (booksToRender.length === 0) {
        booksGrid.innerHTML = '<p style="grid-column: 1/-1; text-align: center; color: #999; padding: 40px;">No books found</p>';
        return;
    }

    booksToRender.forEach(book => {
        const isInCart = appState.cart.some(item => item.id === book.id);
        const bookCard = document.createElement('div');
        bookCard.className = `book-card ${isInCart ? 'selected' : ''}`;
        
        bookCard.innerHTML = `
            <div class="book-icon">📕</div>
            <div class="book-title">${book.title}</div>
            <div class="book-author">by ${book.author}</div>
            <div class="book-year">${book.year}</div>
            <div class="book-buttons">
                <button class="info-btn" data-id="${book.id}">ℹ️ Info</button>
                <button class="add-btn" data-id="${book.id}" ${isInCart ? 'disabled' : ''}>
                    ${isInCart ? 'Added to Cart' : 'Add to Cart'}
                </button>
            </div>
        `;
        
        booksGrid.appendChild(bookCard);
    });

    // Add event listeners to buttons
    document.querySelectorAll('.add-btn').forEach(btn => {
        btn.addEventListener('click', handleAddToCart);
    });
    document.querySelectorAll('.info-btn').forEach(btn => {
        btn.addEventListener('click', handleShowBookInfo);
    });
}

// Function to remove a book from the inventory list
function removeBookFromInventory(bookId) {
    // find index in the main books array
    const idx = books.findIndex(b => b.id === bookId);
    if (idx === -1) return; // not found

    // remove from books array
    books.splice(idx, 1);

    // also update filteredBooks if necessary
    appState.filteredBooks = appState.filteredBooks.filter(b => b.id !== bookId);

    // if the book was in the cart, remove it
    appState.cart = appState.cart.filter(b => b.id !== bookId);

    // re-render UI and stats
    renderBooks(appState.filteredBooks);
    renderCart();
    updateStats();

    showAlert('Book removed from inventory', 'warning');
}

// Handle Add to Cart
function handleAddToCart(e) {
    const bookId = parseInt(e.target.getAttribute('data-id'));
    const book = books.find(b => b.id === bookId);
    
    if (!book) return;
    
    // Check if borrowing limit is reached
    if (appState.cart.length >= appState.borrowingLimit) {
        showAlert(`You've reached your borrowing limit of ${appState.borrowingLimit} books`, 'warning');
        return;
    }
    
    // Check if book is already in cart
    if (appState.cart.some(item => item.id === bookId)) {
        showAlert('This book is already in your cart', 'warning');
        return;
    }
    
    appState.cart.push(book);
    updateStats();
    renderBooks(appState.filteredBooks);
    renderCart();
    showAlert(`"${book.title}" added to cart!`, 'success');
}

// Handle Show Book Info
function handleShowBookInfo(e) {
    const bookId = parseInt(e.target.getAttribute('data-id'));
    const book = books.find(b => b.id === bookId);
    
    if (!book) return;
    
    showBookModal(book);
}

// Show Book Modal
function showBookModal(book) {
    document.getElementById('modalTitle').textContent = book.title;
    document.getElementById('modalAuthor').textContent = book.author;
    document.getElementById('modalYear').textContent = book.year;
    document.getElementById('modalId').textContent = book.id;
    
    document.getElementById('bookModal').style.display = 'block';
}

// Close Book Modal
function closeBookModal() {
    document.getElementById('bookModal').style.display = 'none';
}

// Render Cart
function renderCart() {
    if (appState.cart.length === 0) {
        cartItems.innerHTML = '<p class="empty-message">No books selected yet</p>';
        return;
    }

    cartItems.innerHTML = '';
    appState.cart.forEach(book => {
        const cartItem = document.createElement('div');
        cartItem.className = 'cart-item';
        cartItem.innerHTML = `
            <span class="cart-item-title">${book.title}</span>
            <button class="remove-btn" data-id="${book.id}">Remove</button>
        `;
        cartItems.appendChild(cartItem);
    });

    // Add event listeners to remove buttons
    document.querySelectorAll('.remove-btn').forEach(btn => {
        btn.addEventListener('click', handleRemoveFromCart);
    });

    cartTotalEl.textContent = appState.cart.length;
}

// Handle Remove from Cart
function handleRemoveFromCart(e) {
    const bookId = parseInt(e.target.getAttribute('data-id'));
    const book = appState.cart.find(item => item.id === bookId);
    
    appState.cart = appState.cart.filter(item => item.id !== bookId);
    updateStats();
    renderBooks(appState.filteredBooks);
    renderCart();
    
    if (book) {
        showAlert(`"${book.title}" removed from cart`, 'success');
    }
}

// Handle Checkout
function handleCheckout() {
    if (appState.cart.length === 0) {
        showAlert('Please add books to your cart first', 'warning');
        return;
    }

    const bookTitles = appState.cart.map(b => `"${b.title}"`).join(', ');
    showAlert(`✅ Successfully borrowed ${appState.cart.length} book(s): ${bookTitles}. Enjoy your reading!`, 'success');
    
    // Reset cart
    appState.cart = [];
    updateStats();
    renderBooks(appState.filteredBooks);
    renderCart();
}

// Update Statistics
function updateStats() {
    const totalBorrowed = appState.cart.length;
    const remaining = appState.borrowingLimit - totalBorrowed;
    
    totalBorrowedEl.textContent = totalBorrowed;
    remainingEl.textContent = remaining;
    cartTotalEl.textContent = totalBorrowed;

    // add/remove warning style when limit reached
    if (remaining <= 0) {
        remainingEl.classList.add('limit-reached');
    } else {
        remainingEl.classList.remove('limit-reached');
    }

    // Update checkout button state
    checkoutBtn.disabled = appState.cart.length === 0;

    // show warning when exactly at limit (only once per reach)
    if (remaining === 0) {
        showAlert(`You've reached your borrowing limit of ${appState.borrowingLimit} books`, 'warning');
    }
}

// Show Alert Messages
function showAlert(message, type) {
    // Create alert element
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type}`;
    alertDiv.textContent = message;

    // Insert at the top of container
    document.querySelector('.container').insertBefore(alertDiv, document.querySelector('.header').nextSibling);

    // Auto remove after 4 seconds
    setTimeout(() => {
        alertDiv.remove();
    }, 4000);
}

// Initialize app when DOM is loaded
document.addEventListener('DOMContentLoaded', init);
