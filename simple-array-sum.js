function simpleArraySum(ar) {
    // Write your code here
    let sum = 0;
    //checking that the array is not empty
    if (ar.length > 0){
        for(let i=0; i<ar.length; i++){
            //Assuming that not all items are numbers
            sum +=parseInt(ar[i])
        }
    }
    return sum

}