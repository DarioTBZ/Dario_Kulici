import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.118/build/three.module.js';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );

const renderer = new THREE.WebGLRenderer();
const controls = new OrbitControls(camera, renderer.domElement);

renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );


const geometry = new THREE.BoxGeometry( 1, 1, 1 );
const material = new THREE.MeshBasicMaterial( { color: 0x3157b0 } );
const cube = new THREE.Mesh( geometry, material );
scene.add( cube );

camera.position.z = 5;

const gloader = new GLTFLoader();
gloader.load("./models/mech_drone/scene.gltf", (drone) => {
    scene.add(drone.scene);
});


const light = new THREE.AmbientLight(0xdbb62e)
scene.add(light)

const loader = new THREE.CubeTextureLoader();
const texture = loader.load([
    "./Textures/penguins/arid_rt.jpg", // Positive X (rechts)
    "./Textures/penguins/arid_lf.jpg", // Negative X (links)
    "./Textures/penguins/arid_up.jpg", // Positive Y (oben)
    "./Textures/penguins/arid_dn.jpg", // Negative Y (unten)
    "./Textures/penguins/arid_ft.jpg", // Positive Z (vorne)
    "./Textures/penguins/arid_bk.jpg"  // Negative Z (hinten)
]);
scene.background = texture;


function animate() {      
	requestAnimationFrame( animate );
	renderer.render( scene, camera );
}
animate();




