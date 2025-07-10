// function double(index, array)
// {
//     for(let i = 0; i < array.length; i++){
//         if(i != index && array[index] == array[i]){
//             return 1
//         }
//     }
// }
function double(arr){
    let res_o = {
    }
    arr.forEach(element => {
        if(res_o[element] == undefined){
            res_o[element] = 1
        }
        else{
            res_o[element] +=1
        }
    });
    return res_o
}

function unique(obj){
    let res_ar = []
    for(const el in obj){
        if(obj[el] == 1){
            res_ar.push(Number(el))
        }
    }
    return res_ar
}

function not_unique(obj){
    let res_ar = []
    for(const el in obj){
        if(obj[el] > 1){
            res_ar.push(Number(el))
        }
    }
    return res_ar
}

console.log('Hi')
let ar = [1,2,34,53,23,2,1,13]
// let ar_res = []

// for(let i = 0; i < ar.length; i++){
//     if (ar_res.indexOf(ar[i]) ==-1 && double(i, ar) == 1){
//         ar_res.push(ar[i])
//     }
// }

// console.log(ar_res)

console.log(unique(double(ar)))
console.log(not_unique(double(ar)))

