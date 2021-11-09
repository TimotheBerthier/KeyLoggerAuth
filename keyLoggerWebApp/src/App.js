import './App.css';

const fs = require('browserify-fs');
// const path = require('path');

function App() {
  return (
    <div className="App">
      <header className="App-header">
        {/* <input type='text' id='title' placeholder='enter the file name here'/>
        <br/> */}
        Web application is listening to key strokes !
        <br/>
        <button id='save-button' onClick={() => clearBuffer()}>Clear buffer</button>
        <br/>
        <textarea cols='50' rows='20' type='text' id='text-field' className='text-field'/>
        <br/>
        <button id='save-button' onClick={writeToFile()}>get strokes as CSV</button>
        {/* <a
          href="test.txt"
          download
        >
          Click to download
        </a> */}
        {/* <textarea cols='50' rows='10' type='text' id='text-field2' className='text-field2' value={keyStrokes}/>       */}
      </header>
    </div>
  );
}

function clearBuffer(){
  keyStrokes=['down,keyCode,hours,minutes,seconds,milliseconds'];
  document.getElementById('text-field').value = '';
}

function flattenArray(){
  navigator.clipboard.writeText('test');
  var result = '';
  keyStrokes.forEach(keyEvent => {
    result+=keyEvent;
    result+='\n';
  });
  return result;
}

function writeToFile(){
  return function(){
    console.log('ok')
    var result = flattenArray();
    document.getElementById('text-field').value = result;

    // fs.writeFile('test.txt', flattenArray(), { flag: 'w' }, function(err) {
    //   if (err) 
    //       return console.error(err); 
    //   fs.readFile('test.txt', 'utf-8', function (err, data) {
    //       if (err)
    //           return console.error(err);
    //       console.log(data);
    //   });
    // })
  }
}


let keyStrokes = []
keyStrokes.push('down,keyCode,hours,minutes,seconds,milliseconds')

document.addEventListener('keyup', logKeyUp);
document.addEventListener('keydown', logKeyDown);

function logKeyDown(e) {
  let actualTime = new Date();
  // let time = {
  //   keydown: true,
  //   keycode: e.code,
  //   hour: actualTime.getUTCHours(),
  //   minutes: actualTime.getMinutes(),
  //   seconds: actualTime.getSeconds(),
  //   milliseconds: actualTime.getUTCMilliseconds()
  // }
  let time = `true,${e.code},${actualTime.getUTCHours()},${actualTime.getMinutes()},${actualTime.getSeconds()},${actualTime.getUTCMilliseconds()}`

  keyStrokes.push(time)
}

function logKeyUp(e) {
  let actualTime = new Date();
  let time = `false,${e.code},${actualTime.getUTCHours()},${actualTime.getMinutes()},${actualTime.getSeconds()},${actualTime.getUTCMilliseconds()}`

  keyStrokes.push(time)
}


export default App;
