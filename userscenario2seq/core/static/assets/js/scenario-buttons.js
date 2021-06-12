function addCondition(id){
    //ambil button id
    let splittedId = id.split('-');
    let buttonId = splittedId[3];
    
    //ambil child dari div scenario sesuai button
    let scenarioDiv = document.getElementById(`scenario${buttonId}`)
    let scenarioChilds = scenarioDiv.children
    
    //hitung count
    let childrenCount = scenarioChilds.length;
    let currentIdCount = Math.ceil((childrenCount-3)/2);

    //buat div select
    let divSelect = document.createElement("div");
    divSelect.setAttribute('class','form-group col-md-2');
    divSelect.id=`scenario${buttonId}-select-${currentIdCount}`

    //masukkan select kedalam divSelect
    let s = document.createElement("select");
    s.setAttribute('class', 'form-control');
    s.setAttribute('name',`scenario${buttonId}-tipe${currentIdCount}`);
    s.setAttribute('required', true);

    //masukkan tiap option ke dalam select
    if(buttonId == 0){
        for(let i=0;i<1;i++){
            let o = document.createElement("option");
            if(i == 0){
                o.setAttribute('selected', true);
                o.innerHTML = "When";
            }
            // else{
            //     o.innerHTML = "Then";
            // }
            s.appendChild(o)
        }
    }
    else{
        let o = document.createElement("option");
        o.setAttribute('selected',true);
        o.innerHTML = "Then";
        s.appendChild(o)
    }
    divSelect.appendChild(s)
    
    //buat div input kondisi
    let divInput = document.createElement("div");
    divInput.setAttribute('class','form-group col-md-10');
    divInput.id=`scenario${buttonId}-input-${currentIdCount}`

    //masukkan input pada divInput
    let input = document.createElement("input")
    input.setAttribute('type','text')
    input.setAttribute('class','form-control')
    input.setAttribute('name',`scenario${buttonId}-content${currentIdCount}`)
    input.setAttribute('placeholder','Fill the condition here')
    input.setAttribute('required',true)
    divInput.appendChild(input)
    
    //tambahkan divSelect dan divInput ke scenario
    scenarioDiv.appendChild(divSelect);
    scenarioDiv.appendChild(divInput);

    //tambah value pada jumlah condition
    let conditionCount = document.getElementById(`count${buttonId}`)
    let currentCount = parseInt(conditionCount.value) + 1;
    conditionCount.setAttribute('value',currentCount)
}

function decCondition(id){
    //ambil button id
    let splittedId = id.split('-');
    let buttonId = splittedId[3];
    
    //ambil child dari div scenario sesuai button
    let scenarioDiv = document.getElementById(`scenario${buttonId}`)
    let scenarioChilds = scenarioDiv.children
    
    //hitung count
    let childrenCount = scenarioChilds.length;
    let currentIdCount = Math.ceil((childrenCount-3)/2);

    if(buttonId == 0){
        if(currentIdCount > 3){
            //ambil child yg mau dihapus
            let divSelect = document.getElementById(`scenario${buttonId}-select-${currentIdCount-1}`)
            let divInput = document.getElementById(`scenario${buttonId}-input-${currentIdCount-1}`)
            //hapus child
    
            divSelect.remove()
            divInput.remove()
    
            //kurangi value pada jumlah condition
            let conditionCount = document.getElementById(`count${buttonId}`)
            let currentCount = parseInt(conditionCount.value) - 1;
            conditionCount.setAttribute('value',currentCount)
        }
        else{
            alert("Minimal terdapat 3 kondisi dalam 1 scenario normal yang terdiri dari 1 Given, 1 When, dan 1 Then")
        }
    }
    else{
        if(currentIdCount > 1){
            //ambil child yg mau dihapus
            let divSelect = document.getElementById(`scenario${buttonId}-select-${currentIdCount-1}`)
            let divInput = document.getElementById(`scenario${buttonId}-input-${currentIdCount-1}`)
            //hapus child
    
            divSelect.remove()
            divInput.remove()
    
            //kurangi value pada jumlah condition
            let conditionCount = document.getElementById(`count${buttonId}`)
            let currentCount = parseInt(conditionCount.value) - 1;
            conditionCount.setAttribute('value',currentCount)
        }
        else{
            alert("Minimal terdapat 1 kondisi dalam 1 scenario alternatif dengan tipe Then")
        }
    }

}

function addScenario(){
    //ambil div all scenario
    let allScenario = document.getElementById('all-scenario')
    let childrenCount = allScenario.children.length;
    let newScenarioId = parseInt(childrenCount/2);

    //mulai penambahan scenario
    let rowCount = 1;
    let scenario = document.createElement('div');
    scenario.setAttribute('class','form-row')
    scenario.id = `scenario${newScenarioId}`
    
    //tambahkan hr sebagai pembatas
    let hrScenario = document.createElement('hr');
    hrScenario.setAttribute('class','w-100');
    scenario.appendChild(hrScenario);

    //tambah input hidden jumlah condition
    let conditionCount = document.createElement('input');
    conditionCount.id=`count${newScenarioId}`;
    conditionCount.type="hidden";
    conditionCount.name=`count${newScenarioId}`;
    conditionCount.value="1";
    scenario.appendChild(conditionCount)

    //bikin div nama scenario
    let divScenario = document.createElement("div");
    divScenario.setAttribute('class', 'form-group col-md-12')
    
    //isi div pakai <p> dan input nama scenario
    let textScenario = document.createElement("p");
    textScenario.innerHTML = `Scenario ${newScenarioId+1}`;

    let delScenario = document.createElement("button");
    delScenario.id=`del-${newScenarioId}`
    delScenario.innerHTML="Delete Scenario"
    delScenario.setAttribute('class',"btn btn-danger my-3" );
    delScenario.setAttribute('type','button');
    delScenario.setAttribute('onclick','deleteScenario(this.id)')

    let nameScenario = document.createElement("input");
    nameScenario.setAttribute('type','text')
    nameScenario.setAttribute('class','form-control')
    nameScenario.setAttribute('style',"max-width: 300px")
    nameScenario.setAttribute('name',`name${newScenarioId}`)
    nameScenario.setAttribute('placeholder','Fill the scenario name')
    nameScenario.setAttribute('required',true)
    divScenario.appendChild(textScenario)
    divScenario.appendChild(nameScenario)
    divScenario.appendChild(delScenario)

    //masukkan ke scenario
    scenario.appendChild(divScenario)

    for(let i=0; i<rowCount; i++){
        

        //buat div select
        let divSelect = document.createElement("div");
        divSelect.setAttribute('class','form-group col-md-2');
        divSelect.id=`scenario${newScenarioId}-select-${i}`

        //masukkan select kedalam divSelect
        let s = document.createElement("select");
        s.setAttribute('class', 'form-control');
        s.setAttribute('name',`scenario${newScenarioId}-tipe${i}`);
        s.setAttribute('required', true);

        //masukkan tiap option ke dalam select
        /*
        for(let i=0;i<3;i++){
            let o = document.createElement("option");
            if(i == 0){
                o.setAttribute('selected', true);
                o.innerHTML = "Given";
            }
            else if(i == 1){
                o.innerHTML = "When";
            }
            else{
                o.innerHTML = "Then";
            }
            s.appendChild(o)
        }
        */
        let o = document.createElement("option");
        o.setAttribute('selected',true);
        o.innerHTML = "Then";
        s.appendChild(o)

        divSelect.appendChild(s)
        
        //buat div input kondisi
        let divInput = document.createElement("div");
        divInput.setAttribute('class','form-group col-md-10');
        divInput.id=`scenario${newScenarioId}-input-${i}`

        //masukkan input pada divInput
        let input = document.createElement("input")
        input.setAttribute('type','text')
        input.setAttribute('class','form-control')
        input.setAttribute('name',`scenario${newScenarioId}-content${i}`)
        input.setAttribute('placeholder','Fill the condition here')
        input.setAttribute('required',true)
        divInput.appendChild(input)
        
        //tambahkan divSelect dan divInput ke scenario
        scenario.appendChild(divSelect);
        scenario.appendChild(divInput);
    }

    //tambahkan div berisi button add condition and decrease condition
    let buttonDiv = document.createElement("div");
    buttonDiv.id=`buttons-${newScenarioId}`
    buttonDiv.setAttribute('class','form-group col-md-12 mb-5');
    
    //buat button add condition
    let buttonAdd = document.createElement('button');
    buttonAdd.id = `add-condition-scenario-${newScenarioId}`
    buttonAdd.setAttribute('type','button');
    buttonAdd.setAttribute('class',"btn btn-outline-primary btn-sm-block");
    buttonAdd.setAttribute('onclick','addCondition(this.id)');
    buttonAdd.innerHTML = "+ Add Condition"

    //buat button add condition
    let buttonDec = document.createElement('button');
    buttonDec.id = `dec-condition-scenario-${newScenarioId}`
    buttonDec.setAttribute('type','button');
    buttonDec.setAttribute('class',"btn btn-outline-danger btn-sm-block ml-2");
    buttonDec.setAttribute('onclick','decCondition(this.id)');
    buttonDec.innerHTML = "+ Decrease Condition"
    
    //tambahkan kedua button ke dalam buttonDiv
    buttonDiv.appendChild(buttonAdd)
    buttonDiv.appendChild(buttonDec)

    //masukkan scenario dan buttondiv ke all-scenario
    document.getElementById('all-scenario').appendChild(scenario)
    document.getElementById('all-scenario').appendChild(buttonDiv)

    //tambah value pada scenario-count
    let scenarioCount = document.getElementById('scenario-count')
    let currentValue = scenarioCount.value;
    scenarioCount.value = parseInt(currentValue)+1;
}

function deleteScenario(id){
    let splittedId = id.split('-');
    let idNumber = splittedId[1];
    
    //ambil div scenario dan button yg mau didelete
    if(idNumber > 0){
        let scenario = document.getElementById(`scenario${idNumber}`);
        let buttondiv = document.getElementById(`buttons-${idNumber}`);
        scenario.remove()
        buttondiv.remove()

        //kurangi value pada scenario-count
        let scenarioCount = document.getElementById('scenario-count')
        let currentValue = scenarioCount.value;
        scenarioCount.value = parseInt(currentValue)-1;
    }
}