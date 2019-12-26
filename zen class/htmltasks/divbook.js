     function change(){
        let name23=document.getElementById('hastobechanged').value;
        let name345 =document.getElementById('containername').value;
        let change=document.getElementById(name23);
        change.innerHTML=name345;
        }
         function  adddiv() {  
          var name=document.getElementById('additem').value;
          var div = document.createElement('div');
          var br=document.createElement('br');
          let divid=Math.ceil(Math.random()*100);
           div.innerHTML=name+"  id:"+divid;

          div.className = 'new'; 
          div.name
          div.id=divid;     

       document.getElementsByTagName('body')[0].appendChild(div);
       document.getElementsByTagName('body')[0].appendChild(br);
       
 }