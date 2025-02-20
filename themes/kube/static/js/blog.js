// Blog search and filter functionality
class BlogFilter {
    constructor() {
        this.searchInput = document.getElementById('searchInput');
        this.categoryFilter = document.getElementById('categoryFilter');
        this.blogCards = document.querySelectorAll('.blog-card');
        this.setupEventListeners();
    }

    setupEventListeners() {
        this.searchInput?.addEventListener('input', () => this.filterPosts());
        this.categoryFilter?.addEventListener('change', () => this.filterPosts());
    }

    filterPosts() {
        const searchTerm = this.searchInput?.value.toLowerCase() || '';
        const selectedCategory = this.categoryFilter?.value.toLowerCase() || '';

        this.blogCards.forEach(card => {
            const title = card.querySelector('h2')?.innerText.toLowerCase() || '';
            const excerpt = card.querySelector('.blog-excerpt')?.innerText.toLowerCase() || '';
            const categories = card.dataset.categories?.toLowerCase() || '';
            
            const matchesSearch = title.includes(searchTerm) || excerpt.includes(searchTerm);
            const matchesCategory = !selectedCategory || categories.includes(selectedCategory);

            card.style.display = matchesSearch && matchesCategory ? 'flex' : 'none';
        });
    }
}

// Initialize blog features when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    if (document.querySelector('.blog-container')) {
        new BlogFilter();
    }
});