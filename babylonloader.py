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
          
    import { World } from 'https://cdn.jsdelivr.net/gh/brot-senpai/pde@0.91/bgraph.js';

        const worldData = {
        cameraDist: 4,
        backgroundColor: new BABYLON.Color3(0,0,0),
      }
        var w = new World({canvas, worldData})
        var scene = w.scene;
        w.engine.runRenderLoop(function () {
                    scene.render();
            });

            window.addEventListener("resize", function () {
                    w.engine.resize();
            });
        ControlGrid({scene})
        const sphere = BABYLON.MeshBuilder.CreateSphere("sphere", {});
        const gridData = {
            xmin: -4,
            ymin: -4,
            zmin: 0,
            xmax: 4,
            ymax: 4,
            zmax: 4,
            resolution: 0.5,
            alpha: 0.5,
          }
        var grid = new RectGridClass({scene, gridData});
        var d = %s;
    </script>
		""" % str(x)
  )

