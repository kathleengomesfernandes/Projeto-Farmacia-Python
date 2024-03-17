

function ciclo_trabalho(){		   
    var taus = window.document.getElementById('tau')
    var pris = window.document.getElementById('pri')
    var res = window.document.getElementById('dt')
    var tau_1 = Number(taus.value)
    var pri_1 = Number(pris.value)
    var dts = tau_1/pri_1	
    //dt.value = dts
    res.value = dts    

 }		

 		