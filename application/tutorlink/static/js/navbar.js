let name_plate = document.getElementById('username-plate');
let dropdown = document.getElementById('user-dropdown');

document.addEventListener('click', (evt) =>
{
    let clickTarget = evt.target;

    //user clicks on their "welcome, <user>" button
    if(clickTarget === name_plate)
    {
        //condition is so clicking again closes
        if(dropdown.classList.contains('not-visible'))
        {
            dropdown.classList.remove('not-visible');
            dropdown.classList.add('is-visible');
        }
        else
        {
            dropdown.classList.remove('is-visible');
            dropdown.classList.add('not-visible');
        }
    }
    //condition is for preventing accidental closure if user clicks on the gaps
    else if(clickTarget !== dropdown)
    {
        dropdown.classList.remove('is-visible');
        dropdown.classList.add('not-visible');
    }
});
