#from IPython.display import HTML

class Babylon:
	def __init__(self, backgroundColor=(1, 1, 1)):
		self.backgroundColor = backgroundColor

	def header(self):
		return (
		"""
		<head>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

      <script src="https://code.jquery.com/pep/0.4.2/pep.min.js"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/dat-gui/0.6.2/dat.gui.min.js"></script>
      <script src="https://preview.babylonjs.com/ammo.js"></script>
      <script src="https://preview.babylonjs.com/cannon.js"></script>
      <script src="https://preview.babylonjs.com/Oimo.js"></script>
      <script src="https://preview.babylonjs.com/earcut.min.js"></script>
      <script src="https://preview.babylonjs.com/babylon.js"></script>
      <script src="https://preview.babylonjs.com/materialsLibrary/babylonjs.materials.min.js"></script>
      <script src="https://preview.babylonjs.com/proceduralTexturesLibrary/babylonjs.proceduralTextures.min.js"></script>
      <script src="https://preview.babylonjs.com/postProcessesLibrary/babylonjs.postProcess.min.js"></script>
      <script src="https://preview.babylonjs.com/loaders/babylonjs.loaders.js"></script>
      <script src="https://preview.babylonjs.com/serializers/babylonjs.serializers.min.js"></script>
      <script src="https://preview.babylonjs.com/gui/babylon.gui.min.js"></script>
      <script src="https://preview.babylonjs.com/inspector/babylon.inspector.bundle.js"></script>

    	<style>
        html, body {
          overflow: hidden;
          width: 100%;
          height: 100%;
          margin: 0;
          padding: 0;
        }

        #renderCanvas {
          width: 100%;
          height: 100%;
          touch-action: none;
            }
      </style>
    </head>
    <canvas id="renderCanvas"></canvas>
  """)

	def scene(self):
		return(
		"""		
      
    <script type="text/javascript">
          
    var canvas = document.getElementById("renderCanvas");

    var engine = null;
    var scene = null;
    var sceneToRender = null;
    var createDefaultEngine = function() { return new BABYLON.Engine(canvas, 
      true, { preserveDrawingBuffer: true, stencil: true,  
      disableWebGL2Support: false}); };
    const createScene = function () {
      const scene = new BABYLON.Scene(engine);
      scene.clearColor = new BABYLON.Color3%s;
      const camera = new BABYLON.ArcRotateCamera("Camera", 3 * Math.PI / 2, 
        3 * Math.PI / 8, 30, new BABYLON.Vector3.Zero(), scene)
      camera.attachControl(canvas, true);
      const light = new BABYLON.HemisphericLight("light", 
      new BABYLON.Vector3(1, 1, 0), scene);
      return scene;

    };

    var engine;
    var scene;
    initFunction = async function() {               
      var asyncEngineCreation = async function() {
      try {
        return createDefaultEngine();
        } catch(e) {
        console.log("the available createEngine function failed. Creating the default engine instead");
        return createDefaultEngine();
        }
      }

      engine = await asyncEngineCreation();
      if (!engine) throw 'engine should not be null.';
    	scene = createScene();};
      initFunction().then(() => {sceneToRender = scene        
        engine.runRenderLoop(function () {
        if (sceneToRender && sceneToRender.activeCamera) {
        sceneToRender.render();
          }
      });
      });

      
      window.addEventListener("resize", function () {
          engine.resize();
        });
    </script>
		""" % str(self.backgroundColor)
  )

