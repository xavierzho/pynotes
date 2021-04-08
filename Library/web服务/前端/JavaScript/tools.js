function bubbleSortAsc(arr){
    for(let i = 0; i < arr.length; i++){
                for(let j = 0; j < arr.length - (i + 1); j++){
                    if(arr[j] > arr[j + 1]){
                    //交换两个数位置
                        let tmp = arr[j];
                        arr[j] = arr[j + 1];
                        arr[j + 1] = tmp;
                    }
                }
            }
    }

function bubbleSortDesc(arr){
    for(let i = 0; i < arr.length; i++){
                for(let j = 0; j < arr.length - (i + 1); j++){
                    if(arr[j] < arr[j + 1]){
                    //交换两个数位置
                        let tmp = arr[j];
                        arr[j] = arr[j + 1];
                        arr[j + 1] = tmp;
                    }
                }
            }
    }


function selectSortAsc(arr){
            let i;
    for(i = 0; i <
    length - 1; i++){
                let j;
        for(j = i + 1; j <
        length; j++){
                    if(arr[i] > arr[j]){
                        let tmp = arr[i];
                        arr[i] = arr[j];
                        arr[j] = tmp;
                    }
                }
            }
        }

function selectSortDesc(arr){
            for(let i = 0; i <
    length - 1; i++){
                let j;
                for(j = i + 1; j <
                length; j++){
                    if(arr[i] < arr[j]){
                        let tmp = arr[i];
                        arr[i] = arr[j];
                        arr[j] = tmp;
                    }
                }
            }
        }