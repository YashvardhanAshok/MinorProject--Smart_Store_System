// menu
document.getElementById('menu').addEventListener('click', () => {
  document.querySelector('#menu').classList.toggle('active');


});



  // Get the elements by their class names
  const headOfSigningUp = document.querySelector('.head_of_signing_up');
  const signingUpText = document.querySelector('.SIGNING_UP__text');
  const have_signingUpText = document.querySelector('.have_SIGNING_UP__text');
  // mainbox
  const LOGIN_NAME = document.querySelector('.LOGIN_NAME');

  var toggle = true
  
  // Add a click event listener to the "head_of_signing_up" element
  headOfSigningUp.addEventListener('click', () => {

    signingUpText.classList.toggle('active');
    have_signingUpText.classList.toggle('active');
    LOGIN_NAME.classList.toggle('active');

    const inputField = document.querySelector('.l_pass_Name');
    const label = document.querySelector('#group label');
    inputField.setAttribute('type', 'text');
    inputField.setAttribute('autocomplete', 'one-time-code');

    // Change label text to 'OTP'
    if (toggle) {
      label.textContent = 'OTP';
    }
    else {
      label.textContent = 'Password';

     }
    toggle = !toggle

    document.getElementById('group').classList.toggle('active');
 

      
  });

  
  document.querySelector('.l_SUMET_BU ').addEventListener('click', () => {
  
    window.location.href = `../TOKYUMEI.html?${document.getElementById('l_email_Name').value}` ;
    console.log()

  });
  