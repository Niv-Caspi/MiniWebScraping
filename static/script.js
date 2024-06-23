document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('price_fields').style.display = 'none';
});

function togglePriceFields() {
    var sortBy = document.getElementById('sort_by').value;
    var priceFields = document.getElementById('price_fields');
    if (sortBy === 'price') {
        priceFields.style.display = 'block';
    } else {
        priceFields.style.display = 'none';
    }
}

function validateForm() {
    var url = document.getElementById('url').value;
    var sortBy = document.getElementById('sort_by').value;
    var minPrice = parseFloat(document.getElementById('min_price').value);
    var maxPrice = parseFloat(document.getElementById('max_price').value);
    var error = document.getElementById('error');
    var urlPattern = /^(https?:\/\/)?([a-zA-Z0-9.-]+)(:[0-9]{1,5})?(\/.*)?$/;

    if (!urlPattern.test(url)) {
        error.textContent = "Please enter a valid URL.";
        return false;
    }

    if (!url.startsWith('http://') && !url.startsWith('https://')) {
        error.textContent = "URL must start with http:// or https://.";
        return false;
    }

    if (sortBy === 'price') {
        if (isNaN(minPrice) || minPrice < 0) {
            error.textContent = "Min Price must be a non-negative number.";
            return false;
        }
        if (isNaN(maxPrice) || maxPrice < 0) {
            error.textContent = "Max Price must be a non-negative number.";
            return false;
        }
        if (minPrice > maxPrice) {
            error.textContent = "Min Price cannot be greater than Max Price.";
            return false;
        }
    }

    error.textContent = "";
    return true;
}
