var array = [[['firstName', 'Vasanth'], ['lastName', 'Raja'], ['age', 24], ['role', 'JSWizard']], [['firstName', 'Sri'], ['lastName', 'Devi'], ['age', 28], ['role', 'Coder']]];
var array2=[]
var myobj={}
var myobj2={}
for( let i=0;i<array.length;i++){
    array[i].forEach(function(arrayt){
        myobj[arrayt[0]]=arrayt[1];
    });
    break;
}

for( let i=0;i<array.length;i++){
    array[i].forEach(function(arrayt){
        myobj2[arrayt[0]]=arrayt[1];
    });
}
array2[0]=myobj;
array2[1]=myobj2;
console.log(array2);
