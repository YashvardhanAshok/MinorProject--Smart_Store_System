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
