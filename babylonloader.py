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
  """)

	def scene(self, x):
		return(
		"""
		<canvas id="renderCanvas"></canvas>
      
    <script type="module">
          
    import {DBControl, Axis, World, RectGridClass, Rect3D, locatorClass} from 'https://cdn.jsdelivr.net/gh/brot-senpai/pde@0.98/bgraph.js';
       
       
        var canvas = document.getElementById("renderCanvas"); 
        const engine = new BABYLON.Engine(canvas, true);  
        const scene = new BABYLON.Scene(engine);

        const Data = %s;
        const solution = Data.solution;
        const resolution = Data.resolution;


        const gridData = {
          xmin: Data.xinitial,
          ymin: Data.umin,
          zmin: Data.tinitial,
          xmax: Data.xfinal,
          ymax: Data.umax,
          zmax: Data.tfinal,
          resolution: 0.5,
          alpha: 0.5,
        }
        const dz = Data.tfinal - Data.tinitial;

        const worldData = {
          cameraDist: dz,
          backgroundColor: new BABYLON.Color3(0,0,0),
        }
    
        var grid = new RectGridClass({scene,gridData});  
        var curve = new Rect3D({scene, solution, resolution});
        var db = DBControl({scene, worldData});
    </script>
		""" % str(x)
  )

