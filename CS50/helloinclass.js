document.addEventListener('DOMContentLoaded', function() {              //allows script to be written to later be called and exicuted further down the code
    document.querySelector('form').addEventListener('submit', function(event) {
        let name = document.querySelector('#name').value;
        alert('helo, ' + name);
        event.preventDefault();
    });
});
