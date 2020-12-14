import {addition} from './addition.js';

var createScene = function(props) {
	var {engine, canvas} = props;
    var scene = new BABYLON.Scene(engine);
    const camera = new BABYLON.ArcRotateCamera("Camera", Math.PI / 2, Math.PI / 2, 2, new BABYLON.Vector3(0, 0, 5), scene);
    camera.attachControl(canvas, true);
    const light = new BABYLON.HemisphericLight("light", new BABYLON.Vector3(1, 1, 0), scene);

    const sphere = BABYLON.MeshBuilder.CreateSphere("sphere", {segments: 64, diameter: 2});
    
  return scene;
};

var maf = function(data){
  
  const answer = addition(data);
  return answer;
}

export { createScene, maf };