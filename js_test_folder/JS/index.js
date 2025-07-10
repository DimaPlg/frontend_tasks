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
}

fetchData();
