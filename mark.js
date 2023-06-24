setInterval(setClock ,1000)

const hours=document.querySelector('[hour-hand]')
const minutes=document.querySelector('[minute-hand]')
const seconds=document.querySelector('[second-hand]')


function setClock(){
    const currentTime=new Date();
    let secondsRatio=currentTime.getSeconds()/60;
    let minutesRatio=(secondsRatio + currentTime.getMinutes()) /60;
    let hoursRatio=(minutesRatio + currentTime.getHours())/12;

    setRotation(seconds,secondsRatio);
    setRotation(minutes ,minutesRatio);
    setRotation(hours,hoursRatio);


    function setRotation(element, rotationRatio){
        element.style.setProperty('--rotation', rotationRatio *360);
    }
   
}
setClock();