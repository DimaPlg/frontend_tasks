// import { load_item } from './cart.js';

async function fetchData() {
    fetch('https://fakestoreapi.com/products')
        .then((response) => response.json())
        .then((data) => console.log(data));

    const res = await fetch('https://fakestoreapi.com/products');
    const json = await res.json();
    const ar = Array.from(json)

    let res_ar = []

    // ar.forEach(element => {
    //     if (element.price > 30 && element.rating.rate > 3) {
    //         res_ar.push(element)
    //     }
    // });
    // console.log(res_ar)

    ar.forEach(element => {
        res_ar.push(element)
    });

    const divElement = document.createElement('ul');
    divElement.classList.add('list_style')
    document.body.appendChild(divElement);

    let li_item = document.createElement('li')
    divElement.appendChild(li_item)

    let row_item = document.createElement('div');
    row_item.classList.add('conteiner')
    li_item.appendChild(row_item)

    let counter = 0
    res_ar.forEach(element => {

        if (counter % 4 === 0) {
            li_item = document.createElement('li')
            divElement.appendChild(li_item)

            row_item = document.createElement('div');
            row_item.classList.add('conteiner')
            li_item.appendChild(row_item)
            console.log(counter)
        }
        const item = document.createElement('div');
        item.classList.add('cart');
        row_item.appendChild(item);

        const img_item = document.createElement('img');
        img_item.classList.add('img_aling');
        img_item.src = element.image;
        img_item.alt = 'Описание изображения';
        item.appendChild(img_item);

        const title_item = document.createElement('h2');
        title_item.classList.add('title_description');
        title_item.innerText = element.title;
        item.appendChild(title_item);

        const desc_item = document.createElement('p');
        desc_item.classList.add('description');
        desc_item.innerText = element.description;
        item.appendChild(desc_item)

        const price_item = document.createElement('p');
        price_item.classList.add('price__style');
        price_item.innerText = 'Price: ' + element.price;
        item.appendChild(price_item)

        const rate_item = document.createElement('p');
        rate_item.classList.add('price__style');
        rate_item.innerText = 'Rate: ' + element.rating.rate;
        item.appendChild(rate_item)

        const button_cart = document.createElement('button');
        button_cart.classList.add('button_st');
        button_cart.addEventListener('click', function () {
            const params = new URLSearchParams();

            params.append("category", element.category);
            params.append("description", element.description);
            params.append("id", element.id);
            params.append("image", element.image);
            params.append("price", element.price);
            params.append("count", element['rating'].count);
            params.append("rate", element.rating.rate);
            params.append("title", element.title);

            window.open('../pages/cart.html?' + params, "_blank");
            let value = searchParams.get('category')
            console.log(value)

        });
        item.appendChild(button_cart);

        counter += 1
    });



}

fetchData();
