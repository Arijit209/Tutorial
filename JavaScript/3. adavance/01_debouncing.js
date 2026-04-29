// Debouncing
const debounceField = debounce(fetchData, 500);
document.getElementById('search').addEventListener('input', debounceField)