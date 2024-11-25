// Option functionality
document.querySelector('.option_leter').addEventListener('click', function () {
    document.querySelector('.options').classList.add('active');
    document.querySelectorAll('.option_close').forEach(optionClose => {
        optionClose.classList.add('active');
    });
    document.querySelectorAll('.option_list').forEach(optionList => {
        optionList.classList.add('active');
    });
});

document.querySelector('.options').addEventListener('click', function () {
    this.classList.add('active');
    document.querySelectorAll('.option_close').forEach(optionClose => {
        optionClose.classList.add('active');
    });

    


    document.querySelectorAll('.option_list').forEach(optionList => {
        optionList.classList.add('active');
    });
});

document.querySelector('.option_close').addEventListener('click', function () {
    document.querySelector('.options').classList.remove('active');
    document.querySelectorAll('.option_close').forEach(optionClose => {
        optionClose.classList.remove('active');
    });
    document.querySelectorAll('.option_list').forEach(optionList => {
                setTimeout(() => {
        optionList.classList.remove('active');
        }, 1000); 
    });
});

// Fetch and populate Wish List
fetch('../assets/json/Wish_List.json')
    .then(response => response.json())
    .then(items => {
        let totalBill = 0; 
        let wishListHTML = "<h3>Wish List</h3>";    

        // Render existing wishlist items
        items.forEach(item => {
            const total = (item.price_per_piece * item.quantity).toFixed(2);
            totalBill += parseFloat(total);
            wishListHTML += `
                <div class="item_box">
                    <div class="item_img">
                        <img src="../assets/images/${item.item}.png" alt="${item.item}" width="100%" height="100%">
                    </div>
                    <div class="item_text">
                        <div class="information">x</div>
                        <b>${item.item}</b>
                        <pre>₹${item.price_per_piece} Per Piece</pre>
                        <pre><b>${item.quantity}</b> Remain</pre>
                    </div>
                </div>`;
        });

        // Add search input and add button
        wishListHTML += `
            <div class="item_box add">
                <div class="item_img add" id="wish_add">
                    +     
                </div>
                <div class="search-container">
                    <input type="text" id="searchBar" class="search-bar" placeholder="Search items">
                    <div id="suggestions" class="suggestions"></div>
                </div>
            </div>`;

        document.getElementById('Wish_List').innerHTML = wishListHTML;

        const searchBar = document.getElementById('searchBar');
        const suggestionsDiv = document.getElementById('suggestions');

        const data = [
            { "item": "Apple", "price_per_piece": "80", "quantity": "100" },
            { "item": "Banana", "price_per_piece": "20", "quantity": "150" },
            { "item": "Carrot", "price_per_piece": "30", "quantity": "80" },
            { "item": "Tomato", "price_per_piece": "40", "quantity": "120" },
        ];

        searchBar.addEventListener('input', () => {
            const query = searchBar.value.toLowerCase();
            suggestionsDiv.innerHTML = '';

            if (query) {
                const suggestions = data.filter(item => item.item.toLowerCase().includes(query));
                suggestions.forEach(item => {
                    const suggestion = document.createElement('div');
                    suggestion.textContent = item.item;
                    suggestion.addEventListener('click', () => {
                        searchBar.value = item.item;
                        suggestionsDiv.innerHTML = '';
                    });
                    suggestionsDiv.appendChild(suggestion);
                });
            }
        });

        const attachRemoveFunctionality = (element) => {
element.querySelector('.information').addEventListener('click', function () {
    element.style.display = 'none';
});
        };

        document.getElementById('wish_add').addEventListener('click', function () {
            const searchItem = searchBar.value.toLowerCase();
            const foundItem = data.find(item => item.item.toLowerCase() === searchItem);

            if (foundItem) {
                const newItemHTML = `
                    <div class="item_box">
                        <div class="item_img">
                            <img src="../assets/images/${foundItem.item}.png" alt="${foundItem.item}" width="100%" height="100%">
                        </div>
                        <div class="item_text">
                            <div class="information">x</div>
                            <b>${foundItem.item}</b>
                            <pre>₹${foundItem.price_per_piece} Per Piece</pre>
                            <pre><b>${foundItem.quantity}</b> Remain</pre>
                        </div>
                    </div>`;
                
                const wishlist = document.getElementById('Wish_List');
                const addButtonBox = document.querySelector('.item_box.add');
                addButtonBox.insertAdjacentHTML('beforebegin', newItemHTML);

                // Attach the remove functionality to the new item
                const newItem = wishlist.querySelector('.item_box:not(.add):last-child');
                attachRemoveFunctionality(newItem);

                searchBar.value = '';
            } else {
                alert('Item not found! Please select a valid item from the list.');
            }
        });

        document.querySelectorAll('.item_box').forEach(itemBox => {
            attachRemoveFunctionality(itemBox);
        });
    })
    .catch(error => {
        console.error('Error loading JSON data:', error);
    });



    
// Best Seller
fetch('../assets/json/best_seller.json')
    .then(response => response.json())
    .then(items => {
        let bestSellerHTML = "<H3>Best Seller</H3>";
        items.forEach(item => {
            bestSellerHTML += `
                <div class="item_box">
                    <div class="item_img">
                        <img src="../assets/images/${item.item}.png" alt="${item.item}" width="100%" height="100%">
                    </div>
                    <div class="item_text">
                        <div class="information">!</div>
                        <b>${item.item}</b>
                        <pre>₹${item.price_per_piece} Per Piece</pre>
                        <pre><b>${item.quantity}</b> Remain</pre>
                    </div>
                </div>`;
        });
        document.getElementById('Best_Seller').innerHTML = bestSellerHTML;
    })
    .catch(error => console.error('Error loading JSON data:', error));


       
// Best Seller
fetch('../assets/json/full-list.json')
    .then(response => response.json())
    .then(items => {
        let bestSellerHTML = "<H3>Our Offring</H3>";
        items.forEach(item => {
            bestSellerHTML += `
                <div class="item_box">
                    <div class="item_img">
                        <img src="../assets/images/${item.item}.png" alt="${item.item}" width="100%" height="100%">
                    </div>
                    <div class="item_text">
                        <div class="information">!</div>
                        <b>${item.item}</b>
                        <pre>₹${item.price_per_piece} Per Piece</pre>
                        <pre><b>${item.quantity}</b> Remain</pre>
                    </div>
                </div>`;
        });
        document.getElementById('items').innerHTML = bestSellerHTML;
    })
    .catch(error => console.error('Error loading JSON data:', error));



    


    