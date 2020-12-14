import {createScene} from 'createScene';

var dynamicGrid = function(props){
  
  var scene = createScene(props)
  var psize = 1;
      
      var gridGen =(props)=>{
        var {scene, psize} = props;
        var grid = new BABYLON.GridMaterial("grid", scene);	
        grid.gridRatio = 1;
        grid.opacity = 0.99;
        grid.lineColor = new BABYLON.Color3.Gray();

        const xPlane = new BABYLON.Plane.FromPositionAndNormal(new BABYLON.Vector3(0, 0, 0), new BABYLON.Vector3(1, 0, 0));
        const yPlane = new BABYLON.Plane.FromPositionAndNormal(new BABYLON.Vector3(0, 0, 0), new BABYLON.Vector3(0, 1, 0));
        const zPlane = new BABYLON.Plane.FromPositionAndNormal(new BABYLON.Vector3(0, 0, 0), new BABYLON.Vector3(0, 0, 1));
        var planex = new BABYLON.MeshBuilder.CreatePlane("planex", {size: psize, sourcePlane: xPlane, sideOrientation: BABYLON.Mesh.DOUBLESIDE});
        var planey = new BABYLON.MeshBuilder.CreatePlane("planey", {size: psize, sourcePlane: yPlane, sideOrientation: BABYLON.Mesh.DOUBLESIDE});
        var planez = new BABYLON.MeshBuilder.CreatePlane("planez", {size: psize, sourcePlane: zPlane, sideOrientation: BABYLON.Mesh.DOUBLESIDE});
        
        planex.material = grid;
        planey.material = grid;
        planez.material = grid;
        return [planex, planey, planez, grid];
    }

      var showAxis = function(size) {
      var makeTextPlane = function(text, color, size) {
      var dynamicTexture = new BABYLON.DynamicTexture("DynamicTexture", 50, scene, true);
      dynamicTexture.hasAlpha = true;
      dynamicTexture.drawText(text, 5, 40, "bold 36px Arial", color , "transparent", true);
      var plane = new BABYLON.Mesh.CreatePlane("TextPlane", size, scene, true);
      plane.material = new BABYLON.StandardMaterial("TextPlaneMaterial", scene);
      plane.material.backFaceCulling = false;
      plane.material.specularColor = new BABYLON.Color3(0, 0, 0);
      plane.material.diffuseTexture = dynamicTexture;
      return plane;
      };
    
      var axisX = BABYLON.Mesh.CreateLines("axisX", [ 
        new BABYLON.Vector3.Zero(), new BABYLON.Vector3(size, 0, 0), new BABYLON.Vector3(size * 0.95, 0.05 * size, 0), 
        new BABYLON.Vector3(size, 0, 0), new BABYLON.Vector3(size * 0.95, -0.05 * size, 0)
        ], scene);
      axisX.color = new BABYLON.Color3(1, 0, 0);
      var xChar = makeTextPlane("X", "red", size / 10);
      xChar.position = new BABYLON.Vector3(0.9 * size, -0.05 * size, 0);
      var axisY = BABYLON.Mesh.CreateLines("axisY", [
          new BABYLON.Vector3.Zero(), new BABYLON.Vector3(0, size, 0), new BABYLON.Vector3( -0.05 * size, size * 0.95, 0), 
          new BABYLON.Vector3(0, size, 0), new BABYLON.Vector3( 0.05 * size, size * 0.95, 0)
          ], scene);
      axisY.color = new BABYLON.Color3(0, 1, 0);
      var yChar = makeTextPlane("Y", "green", size / 10);
      yChar.position = new BABYLON.Vector3(0, 0.9 * size, -0.05 * size);
      var axisZ = BABYLON.Mesh.CreateLines("axisZ", [
          new BABYLON.Vector3.Zero(), new BABYLON.Vector3(0, 0, size), new BABYLON.Vector3( 0 , -0.05 * size, size * 0.95),
          new BABYLON.Vector3(0, 0, size), new BABYLON.Vector3( 0, 0.05 * size, size * 0.95)
          ], scene);
      axisZ.color = new BABYLON.Color3(0, 0, 1);
      var zChar = makeTextPlane("Z", "blue", size / 10);
      zChar.position = new BABYLON.Vector3(0, 0.05 * size, 0.9 * size);
    

    var planes = gridGen({scene, psize});
    var planex = planes[0];
    var planey = planes[1];
    var planez = planes[2];
    var grid = planes[3];

    var advancedTexture = BABYLON.GUI.AdvancedDynamicTexture.CreateFullscreenUI("UI", true, scene);
    var slider = new BABYLON.GUI.Slider();
        slider.minimum = 1;
        slider.maximum = 100;
        slider.value = 1;
        slider.height = "20px";
        slider.width = "200px";
        slider.color = "#003399";
        slider.background = "grey";
        slider.top= "20px";
        slider.horizontalAlignment = BABYLON.GUI.Control.HORIZONTAL_ALIGNMENT_CENTER;
        slider.verticalAlignment = BABYLON.GUI.Control.VERTICAL_ALIGNMENT_TOP;
        slider.onValueChangedObservable.add(function (value) {
            axisX.scaling.x = value/2;
            axisY.scaling.y = value/2;
            axisZ.scaling.z = value/2;
            grid.gridRatio = 1/value;
            planex.scaling.x = value;
            planex.scaling.y = value;
            planey.scaling.y = value;
            planey.scaling.x = value;
            planez.scaling.y = value;
            planez.scaling.x = value;
            planex.position.z =value/2;
            planey.position.z = value/2
            planez.position.z = value;
            xChar.scaling.x = value/2;
            xChar.scaling.y = value/2;
            xChar.position.x = value/2;
            yChar.scaling.x = value/2;
            yChar.scaling.y = value/2;
            yChar.position.y = value/2;
            zChar.scaling.x = value/2;
            zChar.scaling.y = value/2;
            zChar.position.x = value/1.85;
            zChar.position.z = value;        
            
            
        });
    
    advancedTexture.addControl(slider);
    };
    showAxis(psize);
    return scene;
}

export {dynamicGrid};