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
        optionList.classList.remove('active');
    });
});


// Wish_List
fetch('../assets/json/Wish_List.json')
    .then(response => response.json())  // Parse JSON data
    .then(items => {
        let totalBill = 0; 

        var a = "<H3>Wish List</H3>";    
        items.forEach(item => {
            const total = (item.price_per_piece * item.quantity).toFixed(2); // Calculate total
            totalBill += parseFloat(total); // Add to total bill

            a += `
                <div class="item_box">
                    <div class="item_img">
                        <img src="../assets/images/${item.item}.png" alt="Girl in a jacket" width="100%" height="100%">
                    </div>
                    <div class="item_text">
                        <div class="information">!</div>
                        <b>${item.item}</b>
                        <pre>₹${item.price_per_piece} Per Piece</pre>
                        <pre><b>${item.quantity}</b> Remain</pre>
                    </div>
                </div>`;
        });

            const b = `
                <div class="item_box add">
                    <div class="item_img add" id="wish_add">
                        +     
                    </div>
                    <div class="search-container">
  <input type="text" id="searchBar" class="search-bar" placeholder="New items">
  <div id="suggestions" class="suggestions"></div>
</div>
                </div>`;

            const c = a + b
        
        
        document.getElementById('Wish_List').innerHTML = c;   

        document.querySelector('#wish_add').addEventListener('click', function() {
            const d = `
                 <div class="item_box">
                    <div class="item_img">
                        <img src="../assets/images/apple.png" alt="Girl in a jacket" width="100%" height="100%">
                    </div>
                    <div class="item_text">
                        <div class="information">!</div>
                        <b>apple</b>
                        <pre>₹300 Per Piece</pre>
                        <pre><b>20</b> Remain</pre>
                    </div>
                </div>`
            const c = a + d + b
        document.getElementById('Wish_List').innerHTML = c;   

            
    
});



 const data = [
    { "item": "Apple", "price_per_piece": "80", "quantity": "100", "expiry": "2024-12-15", "Date_of_manufacture": "2024-11-10" },
    { "item": "Banana", "price_per_piece": "20", "quantity": "150", "expiry": "2024-11-30", "Date_of_manufacture": "2024-11-05" },
    { "item": "Carrot", "price_per_piece": "30", "quantity": "80", "expiry": "2024-12-01", "Date_of_manufacture": "2024-11-12" },
    { "item": "Tomato", "price_per_piece": "40", "quantity": "120", "expiry": "2024-11-25", "Date_of_manufacture": "2024-11-10" },
    { "item": "Cucumber", "price_per_piece": "25", "quantity": "110", "expiry": "2024-12-05", "Date_of_manufacture": "2024-11-15" },
    { "item": "Lettuce", "price_per_piece": "50", "quantity": "70", "expiry": "2024-11-28", "Date_of_manufacture": "2024-11-10" },
    { "item": "Potato", "price_per_piece": "20", "quantity": "200", "expiry": "2025-01-10", "Date_of_manufacture": "2024-10-30" },
    { "item": "Onion", "price_per_piece": "25", "quantity": "150", "expiry": "2025-02-20", "Date_of_manufacture": "2024-10-25" },
    { "item": "Garlic", "price_per_piece": "10", "quantity": "300", "expiry": "2025-03-15", "Date_of_manufacture": "2024-09-05" },
    { "item": "Ginger", "price_per_piece": "60", "quantity": "100", "expiry": "2025-01-30", "Date_of_manufacture": "2024-10-10" },
    { "item": "Milk", "price_per_piece": "45", "quantity": "200", "expiry": "2024-11-28", "Date_of_manufacture": "2024-11-05" },
    { "item": "Cheese", "price_per_piece": "180", "quantity": "60", "expiry": "2025-02-10", "Date_of_manufacture": "2024-10-18" },
    { "item": "Butter", "price_per_piece": "120", "quantity": "70", "expiry": "2025-03-05", "Date_of_manufacture": "2024-09-30" },
    { "item": "Yogurt", "price_per_piece": "50", "quantity": "150", "expiry": "2024-12-05", "Date_of_manufacture": "2024-11-15" },
    { "item": "Bread", "price_per_piece": "35", "quantity": "100", "expiry": "2024-11-20", "Date_of_manufacture": "2024-11-05" },
    { "item": "Rice", "price_per_piece": "90", "quantity": "50", "expiry": "2025-06-15", "Date_of_manufacture": "2024-08-30" },
    { "item": "Pasta", "price_per_piece": "70", "quantity": "60", "expiry": "2025-07-10", "Date_of_manufacture": "2024-09-10" },
    { "item": "Cereal", "price_per_piece": "150", "quantity": "40", "expiry": "2025-01-25", "Date_of_manufacture": "2024-10-10" }
  ];

  const searchBar = document.getElementById('searchBar');
  const suggestionsDiv = document.getElementById('suggestions');

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














    })
    .catch(error => {
        console.error('Error loading JSON data:', error); // Log error if any
    });





// surch

 



















// best_sller
fetch('../assets/json/best_seller.json')
    
    .then(response => response.json())  // Parse JSON data
    .then(items => {
        const billSummaryContainer = document.getElementById('bill_summary_container');

        let totalBill = 0;  // Initialize the total bill

        // Loop through the items array to generate HTML for the items
        items.forEach(item => {
            const total = (item.price_per_piece * item.quantity).toFixed(2); // Calculate total
            totalBill += parseFloat(total); // Add to total bill

            document.getElementById('Best_Seller').innerHTML += `
                <div class="item_box">
                    <div class="item_img">
                        <img src="../assets/images/${item.item}.png" alt="Girl in a jacket" width="100%" height="100%">
                    </div>
                    <div class="item_text">
                        <div class="information">!</div>
                        <b>${item.item}</b>
                        <pre>₹${item.price_per_piece} Per Piece</pre>
                        <pre><b>${item.quantity}</b> Remain</pre>
                    </div>
                </div>`;
        });

    })
    .catch(error => {
        console.error('Error loading JSON data:', error); // Log error if any
    });