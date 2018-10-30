const nombreInput = document.querySelector('input[name=nombre]');
const slugInput = document.querySelector('input[name=slug]');

const slugify = (val) => {

    return val.toString().toLowerCase().trim()
        .replace(/&/g, '-and-')         // Replace & with 'and'
        .replace(/[\s\W-]+/g, '-')      // Replace spaces, non-word characters and dashes with a single dash (-)

};

nombreInput.addEventListener('keyup', (e) => {
    slugInput.setAttribute('value', slugify(nombreInput.value));
});
