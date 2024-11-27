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

// optin end




document.querySelector('.bill').addEventListener('click', function() {
    document.querySelector('.bill_summary').classList.add('active');    
});

document.querySelector('.bill_summary_box_close').addEventListener('click', function() {
    document.querySelector('.bill_summary').classList.remove('active');    
});

document.querySelector('.book_button').addEventListener('click', function() {
    document.querySelector('.book_button_bar').classList.add('active');    
    document.querySelector('.payment').classList.add('active');    
    // document.querySelector('.book_button').innerHTML = "";    

});





fetch('../assets/json/cart.json')
    
    .then(response => response.json())  // Parse JSON data
    .then(items => {
        const itemContainer = document.getElementById('item_container');
        const billSummaryContainer = document.getElementById('bill_summary_container');

        let totalBill = 0;  // Initialize the total bill

        // Loop through the items array to generate HTML for the items
        items.forEach(item => {
            const total = (item.price_per_piece * item.quantity).toFixed(2); // Calculate total
            totalBill += parseFloat(total); // Add to total bill

            itemContainer.innerHTML += `
                <div class="item_box">
                    <div class="item_img">
                        <img src="../assets/images/${item.item}.png" alt="Girl in a jacket" width="100%" height="100%">
                    </div>
                    <div class="item_text">
                        <div class="information">!</div>
                        <b>${item.item}</b>
                        <pre>₹${item.price_per_piece} Per Piece</pre>
                        <pre><b>₹${total}</b> for ${item.quantity} Pieces</pre>
                    </div>
                </div>`;
        });

        // Create a table to display the bill summary
        let tableHTML = `
            <table id="customers">
                <tr>
                    <th>Item</th>
                    <th>Quantity</th>
                    <th>Price</th>
                </tr>
        `;

        // Add each item to the table
        items.forEach(item => {
            const total = (item.price_per_piece * item.quantity).toFixed(2); // Calculate total for the item
            tableHTML += `
                <tr>
                    <td><b>${item.item}</b></td>
                    <td>X${item.quantity}</td>
                    <td>₹${total}</td>
                </tr>
                <tr>
                    <td>Per Piece</td>
                    <td>1</td>
                    <td>₹${item.price_per_piece}</td>
                </tr>
            `;
        });

        // Add GST, platform fee, and total bill rows
        const gst = (totalBill * 0.18).toFixed(2);  // Assuming GST is 18%
        const platformFee = 10; // Example platform fee
        const finalTotal = (parseFloat(totalBill) + parseFloat(gst) + platformFee).toFixed(2);

        tableHTML += `
            <tr>
                <td><b>GST</b></td>
                <td></td>
                <td>₹${gst}</td>
            </tr>
            <tr>
                <td>Platform Fee</td>
                <td></td>
                <td>₹${platformFee}</td>
            </tr>
            <tr>
                <td><b>Total</b></td>
                <td></td>
                <td>₹${finalTotal}</td>
            </tr>
        </table>`;

        // Insert the table into the bill summary container
        billSummaryContainer.innerHTML = tableHTML;
        document.querySelector('#total_price').innerHTML = finalTotal;
    })
    .catch(error => {
        console.error('Error loading JSON data:', error); // Log error if any
    });
    

// qr
            function generateQRCode() {
            const qrCodeContainer = document.getElementById("qrcode");

            // Clear any existing QR Code
            qrCodeContainer.innerHTML = "";

            // Define the values
            const data = {
                name: "yash",
                email: "yashvardhan577@gmail.com",
                customer_id: "10"
            };

            // Convert the data to a JSON string
            const jsonData = JSON.stringify(data);

            // Generate the QR code
            new QRCode(qrCodeContainer, {
                text: jsonData,
                width: 60,
                height: 60,
            });
}
        
generateQRCode()



    // pay
    





    document.querySelector('.nfc').addEventListener('click', function () {

        document.querySelector('.nfc').classList.add('active');

        setTimeout(() => {
            window.location.href = '../pay2/';
        }, 2000); 
    });

    document.querySelector('.Check_Out_At_Cashier').addEventListener('click', function () {

        document.querySelector('.Check_Out_At_Cashier').classList.add('active');

        setTimeout(() => {
            window.location.href = '../pay/';
        }, 2000); 
    });





