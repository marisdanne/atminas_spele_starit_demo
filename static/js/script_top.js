
//no adreses iegūst vārdu un ievieto to virsrakstā
let adrese = window.location.hash;
adrese = adrese.replace('#','');
adrese = decodeURI(adrese);
adrese = adrese.split(",");

let vards   = adrese[0]
let vecums  = adrese[1]
let regions = adrese[2]
let klikski = adrese[3]
let laiks   = adrese[4]
document.querySelector('.virsraksts').innerHTML = 'Apsveicam '+vards+', klikšķi:'+klikski+', sekundes:'+laiks;


let datums = new Date();
let datumsString = datums.getFullYear()+'-'+datums.getMonth()+'-'+datums.getDate()


/*
let topsJson = [
    {
      "id": 0,
      "vards": "Liene",
      "klase": "10b",
      "laiks": "500",
      "klikski": "35",
      "datums": "2021-11-24",
      "piezimes": ""
    },
    {
        "id": 1,
        "vards": "Jānis",
        "klase": "10b",
        "laiks": "500",
        "klikski": "35",
        "datums": "2021-11-24",
        "piezimes": ""
    },
    {
        "id": 2,
        "vards": "Jana",
        "klase": "10b",
        "laiks": "500",
        "klikski": "35",
        "datums": "2021-11-24",
        "piezimes": ""
    }
  ]
  */



  async function iegutDatusNoApi(url)
  {
    let datiNoServera = await fetch(url);
    let datiJson = await datiNoServera.json();
    return datiJson;
  }

  
async function atlasitTop()
{

    //let topsJson = await iegutDatusNoApi('https://armandspucs.github.io/atminas_spele_pabeigts_2/rezultati.json');
    let topsJson = await iegutDatusNoApi('topData');
    //console.log(datiJson);

  for (i = 0; i < topsJson.length; i++)
  {
      

      let tabula = document.querySelector(".tops");

      

      tabula.innerHTML = tabula.innerHTML+`
      <tr id="`+topsJson[i]['id']+`">
      <td> `+topsJson[i]['vards']+` </td>
      <td> `+topsJson[i]['skola']+` </td>
      <td> `+topsJson[i]['vecums']+` </td>
      <td> `+topsJson[i]['laiks']+` </td>
      <td> `+topsJson[i]['klikski']+` </td>
      <td> `+topsJson[i]['datums']+` </td>
      </tr>`;

  }

}

atlasitTop();



function pievienotTop()
{
    let tabula = document.querySelector(".tops");


    tabula.innerHTML = tabula.innerHTML+`
    <tr id="jauns">
    <td> `+vards+` </td>
    <td> `+vecums+` </td>
    <td> `+laiks+` </td>
    <td> `+klikski+` </td>
    <td> `+datumsString+` </td>
    </tr>`;
}


