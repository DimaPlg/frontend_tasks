async function load_item() {
    const params = new URLSearchParams(window.location.search);

    const divElement = document.createElement('ul');
    divElement.classList.add('list_style')
    document.body.appendChild(divElement);

    let li_item = document.createElement('li')
    divElement.appendChild(li_item)

    let row_item = document.createElement('div');
    row_item.classList.add('conteiner')
    li_item.appendChild(row_item)

    const item = document.createElement('div');
    item.classList.add('cart');
    row_item.appendChild(item);

    const img_item = document.createElement('img');
    img_item.classList.add('img_aling');
    img_item.src = params.get('image');
    img_item.alt = 'Описание изображения';
    item.appendChild(img_item);

    const title_item = document.createElement('h2');
    title_item.classList.add('title_description');
    title_item.innerText = params.get('title');
    item.appendChild(title_item);

    const desc_item = document.createElement('p');
    desc_item.classList.add('description');
    desc_item.innerText = params.get('description');
    item.appendChild(desc_item)

    const price_item = document.createElement('p');
    price_item.classList.add('price__style');
    price_item.innerText = 'Price: ' + params.get('price');
    item.appendChild(price_item)

    const rate_item = document.createElement('p');
    rate_item.classList.add('price__style');
    rate_item.innerText = 'Rate: ' + params.get('rate');
    item.appendChild(rate_item)
    console.log(params.get('category'))
    console.log(params.get('description'))
    console.log(params.get('id'))
    console.log(params.get('image'))
    console.log(params.get('price'))
    console.log(params.get('count'))
    console.log(params.get('rate'))
    console.log(params.get('title'))
}

load_item()
