// Add click event listener to all profiles
document.querySelectorAll('.profile').forEach(profile => {
    profile.addEventListener('click', function() {
        document.querySelectorAll('.profile').forEach(p => p.classList.remove('active'));
        this.classList.add('active');
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



