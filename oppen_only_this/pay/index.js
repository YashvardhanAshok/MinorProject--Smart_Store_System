document.querySelectorAll('.profile').forEach(profile => {
    profile.addEventListener('click', function () {
        // Remove the 'active' class from all profiles

        document.querySelectorAll('.profile').forEach(p => p.classList.remove('active'));

        // Add the 'active' class to the clicked profile
        this.classList.add('active');

        // Add 'active' class to the element with the class 'disply_logo'
        const displayLogo = document.querySelector('.disply_logo');
        if (displayLogo) {
            displayLogo.classList.add('active');
        }
        
        const option_leter_name = document.querySelector('.option_leter_name');
        if (option_leter_name) {
            option_leter_name.classList.add('active');
        }
        

        setTimeout(() => {
            window.location.href = '../interface-2/';
        }, 5000); 
    });
});



// document.querySelector('.profile').addEventListener('click', function() {
//     document.querySelector('.profile').classList.add('active');
// });



// document.querySelector('.bill_summary_box_close').addEventListener('click', function() {
//     document.querySelector('.bill_summary').classList.remove('active');
// });

// document.querySelector('.book_button').addEventListener('click', function() {
//     document.querySelector('.book_button_bar').classList.add('active');

// });


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
                width: 250,
                height: 250,
            });
}
        
generateQRCode()


