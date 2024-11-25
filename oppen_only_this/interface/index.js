
fetch('../assets/json/cart.json')
    
    .then(response => response.json())  // Parse JSON data
    .then(items => {

        let totalBill = 0;  

        var a =""
        items.forEach(item => {
            const total = (item.price_per_piece * item.quantity).toFixed(2); // Calculate total
            totalBill += parseFloat(total); // Add to total bill

             a += `
                <div class="item_box">

                     <!-- <div class="information">!</div> -->

                    <div class="item_img">
                        <img src="../assets/images/${item.item}.png" alt="Girl in a jacket" width="100%" height="100%">
                    </div>
                    <div class="item_text">
                        <b>${item.item}</b>
                        <pre>₹${item.price_per_piece} Per Piece</pre>
                    </div>
                </div>`;
            
            
            
            
        });
        document.getElementById('listcontaner_id').innerHTML = a;
        document.getElementById('whish_List').innerHTML = a ;


    })
    .catch(error => {
        console.error('Error loading JSON data:', error); // Log error if any
    });