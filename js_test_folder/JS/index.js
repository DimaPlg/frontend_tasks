async function fetchData() {
    fetch('https://fakestoreapi.com/products')
        .then((response) => response.json())
        .then((data) => console.log(data));

    const res = await fetch('https://fakestoreapi.com/products');
    const json = await res.json();
    const ar = Array.from(json)

    let res_ar = []

    ar.forEach(element => {
        if (element.price > 30 && element.rating.rate > 3) {
            res_ar.push(element)
        }
    });
    console.log(res_ar)

    const divElement = document.createElement('div');
    divElement.classList.add('new-div');
    document.body.appendChild(divElement)

    const text_box = document.createElement('p');
    text_box.classList.add('text');
    text_box.innerText = 'Hi guys!'
    divElement.appendChild(text_box)



}

fetchData();
