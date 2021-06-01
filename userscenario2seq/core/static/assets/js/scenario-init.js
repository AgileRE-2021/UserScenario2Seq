let rowCount = 3;
let scenario = document.createElement('div');
scenario.setAttribute('class','form-row')
scenario.id = `scenario0`

//tambahkan hr sebagai pembatas
let hrScenario = document.createElement('hr');
hrScenario.setAttribute('class','w-100');
scenario.appendChild(hrScenario);

//tambah input hidden jumlah condition
let conditionCount = document.createElement('input');
conditionCount.id="count0";
conditionCount.type="hidden";
conditionCount.name="count0";
conditionCount.value="3";
scenario.appendChild(conditionCount)

//bikin div nama scenario
let divScenario = document.createElement("div");
divScenario.setAttribute('class', 'form-group col-md-12')

//isi div pakai <p> dan input nama scenario
let textScenario = document.createElement("p");
textScenario.innerHTML = "Scenario 1";

/*
let delScenario = document.createElement("button");
delScenario.id="del-0"
delScenario.innerHTML="Delete Scenario"
delScenario.setAttribute('class',"btn btn-danger my-3" );
delScenario.setAttribute('type','button');
delScenario.setAttribute('onclick','deleteScenario(this.id)')*/

let nameScenario = document.createElement("input");
nameScenario.setAttribute('type','text')
nameScenario.setAttribute('class','form-control')
nameScenario.setAttribute('style',"max-width: 300px")
nameScenario.setAttribute('name',`name0`)
nameScenario.setAttribute('value','Normal')
nameScenario.setAttribute('disabled',true)
nameScenario.setAttribute('placeholder','Fill the scenario name')
nameScenario.setAttribute('required',true)

divScenario.appendChild(textScenario)
divScenario.appendChild(nameScenario)
//divScenario.appendChild(delScenario)

//masukkan ke scenario
scenario.appendChild(divScenario)

for(let i=0; i<rowCount; i++){
    //buat div select
    let divSelect = document.createElement("div");
    divSelect.setAttribute('class','form-group col-md-2');
    divSelect.id=`scenario0-select-${i}`

    //masukkan select kedalam divSelect
    let s = document.createElement("select");
    s.setAttribute('class', 'form-control');
    s.setAttribute('name',`scenario0-tipe${i}`);
    s.setAttribute('required', true);

    //masukkan tiap option ke dalam select
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
    divSelect.appendChild(s)
    
    //buat div input kondisi
    let divInput = document.createElement("div");
    divInput.setAttribute('class','form-group col-md-10');
    divInput.id=`scenario0-input-${i}`

    //masukkan input pada divInput
    let input = document.createElement("input")
    input.setAttribute('type','text')
    input.setAttribute('class','form-control')
    input.setAttribute('name',`scenario0-content${i}`)
    input.setAttribute('placeholder','Fill the condition here')
    input.setAttribute('required',true)
    divInput.appendChild(input)
    
    //tambahkan divSelect dan divInput ke scenario
    scenario.appendChild(divSelect);
    scenario.appendChild(divInput);
}

//tambahkan div berisi button add condition and decrease condition
let buttonDiv = document.createElement("div");
buttonDiv.id="buttons-0"
buttonDiv.setAttribute('class','form-group col-md-12 mb-5');

//buat button add condition
let buttonAdd = document.createElement('button');
buttonAdd.id = "add-condition-scenario-0"
buttonAdd.setAttribute('type','button');
buttonAdd.setAttribute('class',"btn btn-outline-primary btn-sm-block");
buttonAdd.setAttribute('onclick','addCondition(this.id)');
buttonAdd.innerHTML = "+ Add Condition"

//buat button add condition
let buttonDec = document.createElement('button');
buttonDec.id = "dec-condition-scenario-0"
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