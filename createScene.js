var createScene = function(props) {
  var {engine, canvas} = props;
    
    var scene = new BABYLON.Scene(engine);
    scene.clearColor = BABYLON.Color3.White();
    const camera = new BABYLON.ArcRotateCamera("Camera", 3 * Math.PI / 2, 
        3 * Math.PI / 8, 30, new BABYLON.Vector3.Zero(), scene)
    camera.attachControl(canvas, true);
    const light = new BABYLON.HemisphericLight("light", new BABYLON.Vector3(1, 1, 0), scene);
    
  return scene;
};

export { createScene };