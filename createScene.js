import {addition} from './addition';

var createScene = function(props) {
	var {engine, canvas, data} = props;
    var scene = new BABYLON.Scene(engine);
    const camera = new BABYLON.ArcRotateCamera("Camera", Math.PI / 2, Math.PI / 2, 2, new BABYLON.Vector3(0, 0, 5), scene);
    camera.attachControl(canvas, true);
    const light = new BABYLON.HemisphericLight("light", new BABYLON.Vector3(1, 1, 0), scene);

    const sphere = BABYLON.MeshBuilder.CreateSphere("sphere", {segments: 64, diameter: 2});
    console.log(addition(data))
  return scene;
};

export { createScene };