

const array: number[] = [0,0,1,1,1,2,2,3,3,4]



const removeDuplicates = (nums: number[])=>{
    
    let uniqueArray: number[] = []

    for(let i = 0; i < nums.length; i++){
        
        if(!uniqueArray.includes(nums[i])){
            uniqueArray.push(nums[i])
        }

    }

   

    let k = uniqueArray.length
    for(let i = 0; i < k; i++){
        nums[i] = uniqueArray[i]
    }
    return k
}

removeDuplicates(array)