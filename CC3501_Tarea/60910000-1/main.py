"""
Refactor: nombres en camelCase, comentarios naturales.
Mantiene la misma lógica original.
"""

import pyglet
from pyglet.window import key
from OpenGL.GL import *
import numpy as np
import os

from . import transformations as tr
from .scene_graph import SceneGraphNode as HierarchyNode
from .geometry import create_cube as createCube, create_sphere as createSphere, create_cylinder as createCylinder


# Window size
WIDTH = 1280
HEIGHT = 720

class RenderProgram:
    # Compila y administra shaders
    def __init__(self, vertex_source, fragment_source):
        self.program = self.compileGLSL(vertex_source, fragment_source)

    def compileGLSL(self, vertex_source, fragment_source):
        vertex_shader = glCreateShader(GL_VERTEX_SHADER)
        glShaderSource(vertex_shader, vertex_source)
        glCompileShader(vertex_shader)
        self.validateCompilation(vertex_shader, "VERTEX")


        fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
        glShaderSource(fragment_shader, fragment_source)
        glCompileShader(fragment_shader)
        self.validateCompilation(fragment_shader, "FRAGMENT")

        program = glCreateProgram()
        glAttachShader(program, vertex_shader)
        glAttachShader(program, fragment_shader)
        glLinkProgram(program)
        self.validateCompilation(program, "PROGRAM")

        glDeleteShader(vertex_shader)
        glDeleteShader(fragment_shader)
        return program

    def validateCompilation(self, handle, kind):
        if kind != "PROGRAM":
            ok = glGetShaderiv(handle, GL_COMPILE_STATUS)
            if not ok:
                info = glGetShaderInfoLog(handle)
                print(f"SHADER {kind} ERROR:\n{info.decode()}")
        else:
            ok = glGetProgramiv(handle, GL_LINK_STATUS)
            if not ok:
                info = glGetProgramInfoLog(handle)
                print(f"PROGRAM LINK ERROR:\n{info.decode()}")

    def useProgram(self):
        glUseProgram(self.program)


    def getProgramID(self):
        return self.program



# ============================================================
# VERSIONES DEL PERSONAJE - Elige tu favorita
# Cambia el número en la línea ACTIVE_VERSION = X
# ============================================================

ACTIVE_VERSION = 5  # <-- CAMBIA ESTE NÚMERO (1-5)

def buildPlayerModel():
    # Construye el modelo con nodos y devolve un diccionario de referencias
    boxMesh = createCube()
    ballMesh = createSphere()
    tubeMesh = createCylinder()

    sceneRoot = HierarchyNode("root")
    sceneRoot.transform = tr.translate(0, 0, 0)

    # Selección de versión
    if ACTIVE_VERSION == 1:
        # VERSIÓN 1: ATLETA PROPORCIONADO (Actual - Realista)
        # Torso mediano, brazos delgados, piernas atléticas
        torsoScale = (0.6, 1.0, 0.35)
        torsoColor = [0.2, 0.3, 0.8]  # Azul
        neckScale = (0.15, 0.25, 0.15)
        headScale = (0.45, 0.5, 0.45)
        skinColor = [0.9, 0.7, 0.6]
        shoulderScale = 0.2
        armThickness = 0.12
        legThickness = 0.18
        pantsColor = [0.1, 0.1, 0.1]  # Negro
        shoesColor = [0.3, 0.2, 0.1]  # Café
        
    elif ACTIVE_VERSION == 2:
        # VERSIÓN 2: SUPERHÉROE MUSCULOSO
        # Torso ancho, brazos gruesos, aspecto poderoso
        torsoScale = (0.8, 1.1, 0.4)
        torsoColor = [0.8, 0.1, 0.1]  # Rojo intenso
        neckScale = (0.2, 0.2, 0.2)
        headScale = (0.4, 0.45, 0.4)
        skinColor = [0.95, 0.8, 0.7]
        shoulderScale = 0.28
        armThickness = 0.18
        legThickness = 0.24
        pantsColor = [0.0, 0.0, 0.5]  # Azul oscuro
        shoesColor = [0.8, 0.7, 0.0]  # Dorado
        
    elif ACTIVE_VERSION == 3:
        # VERSIÓN 3: PERSONAJE CARTOON/ANIME
        # Cabeza grande, cuerpo pequeño, estilo caricatura
        torsoScale = (0.5, 0.8, 0.3)
        torsoColor = [1.0, 0.5, 0.0]  # Naranja
        neckScale = (0.12, 0.18, 0.12)
        headScale = (0.6, 0.65, 0.6)  # Cabeza grande
        skinColor = [1.0, 0.9, 0.8]
        shoulderScale = 0.18
        armThickness = 0.1
        legThickness = 0.14
        pantsColor = [0.2, 0.6, 0.3]  # Verde
        shoesColor = [0.9, 0.9, 0.9]  # Blanco
        
    elif ACTIVE_VERSION == 4:
        # VERSIÓN 4: ROBOT/MECÁNICO
        # Formas angulares, colores metálicos
        torsoScale = (0.7, 0.95, 0.5)
        torsoColor = [0.3, 0.3, 0.35]  # Gris metálico
        neckScale = (0.18, 0.22, 0.18)
        headScale = (0.5, 0.45, 0.5)  # Cabeza cúbica
        skinColor = [0.6, 0.6, 0.65]  # Gris claro
        shoulderScale = 0.25
        armThickness = 0.15
        legThickness = 0.2
        pantsColor = [0.15, 0.15, 0.2]  # Gris oscuro
        shoesColor = [0.4, 0.2, 0.0]  # Café oxidado
        
    else:  # ACTIVE_VERSION == 5
        # VERSIÓN 5: ELEGANTE/ESTILIZADO
        # Proporciones alargadas, colores sofisticados
        torsoScale = (0.55, 1.15, 0.32)
        torsoColor = [0.15, 0.15, 0.25]  # Azul oscuro elegante
        neckScale = (0.13, 0.28, 0.13)
        headScale = (0.42, 0.48, 0.42)
        skinColor = [0.85, 0.65, 0.55]
        shoulderScale = 0.19
        armThickness = 0.11
        legThickness = 0.16
        pantsColor = [0.25, 0.25, 0.3]  # Gris carbón
        shoesColor = [0.1, 0.1, 0.15]  # Negro brillante

    trunk = sceneRoot.add_child(HierarchyNode("torso"))
    trunk.mesh = boxMesh
    trunk.transform = tr.matmul([tr.scale(torsoScale[0], torsoScale[1], torsoScale[2])])
    trunk.color = torsoColor

    neckJoint = trunk.add_child(HierarchyNode("neck"))
    neckJoint.mesh = tubeMesh
    neckJoint.transform = tr.matmul([tr.translate(0, 0.55, 0), tr.scale(neckScale[0], neckScale[1], neckScale[2])])
    neckJoint.color = skinColor


    headNode = neckJoint.add_child(HierarchyNode("head"))
    headNode.mesh = ballMesh
    headNode.transform = tr.matmul([tr.translate(0, 0.35, 0), tr.scale(headScale[0], headScale[1], headScale[2])])
    headNode.color = skinColor

    leftShoulderJoint = trunk.add_child(HierarchyNode("left_shoulder"))
    leftShoulderJoint.mesh = ballMesh
    leftShoulderJoint.transform = tr.matmul([tr.translate(-0.4, 0.4, 0), tr.scale(shoulderScale, shoulderScale, shoulderScale)])
    leftShoulderJoint.color = torsoColor

    leftUpperArm = leftShoulderJoint.add_child(HierarchyNode("left_upper_arm"))
    leftUpperArm.mesh = tubeMesh
    leftUpperArm.transform = tr.matmul([tr.translate(0, -0.35, 0), tr.scale(armThickness, 0.7, armThickness)])
    leftUpperArm.color = torsoColor
    leftElbowJoint = leftUpperArm.add_child(HierarchyNode("left_elbow"))
    leftElbowJoint.mesh = ballMesh
    leftElbowJoint.transform = tr.matmul([tr.translate(0, -0.45, 0), tr.scale(1.1, 0.25, 1.1)])
    leftElbowJoint.color = skinColor

    leftForearm = leftElbowJoint.add_child(HierarchyNode("left_forearm"))
    leftForearm.mesh = tubeMesh
    leftForearm.transform = tr.matmul([tr.translate(0, -0.35, 0), tr.scale(0.95, 0.7, 0.95)])
    leftForearm.color = skinColor

    leftHandJoint = leftForearm.add_child(HierarchyNode("left_hand"))
    leftHandJoint.mesh = ballMesh
    leftHandJoint.transform = tr.matmul([tr.translate(0, -0.5, 0), tr.scale(1.2, 0.35, 1.2)])
    leftHandJoint.color = skinColor


    rightShoulderJoint = trunk.add_child(HierarchyNode("right_shoulder"))
    rightShoulderJoint.mesh = ballMesh
    rightShoulderJoint.transform = tr.matmul([tr.translate(0.4, 0.4, 0), tr.scale(shoulderScale, shoulderScale, shoulderScale)])
    rightShoulderJoint.color = torsoColor
    rightUpperArm = rightShoulderJoint.add_child(HierarchyNode("right_upper_arm"))
    rightUpperArm.mesh = tubeMesh
    rightUpperArm.transform = tr.matmul([tr.translate(0, -0.35, 0), tr.scale(armThickness, 0.7, armThickness)])
    rightUpperArm.color = torsoColor

    rightElbowJoint = rightUpperArm.add_child(HierarchyNode("right_elbow"))
    rightElbowJoint.mesh = ballMesh
    rightElbowJoint.transform = tr.matmul([tr.translate(0, -0.45, 0), tr.scale(1.1, 0.25, 1.1)])
    rightElbowJoint.color = skinColor

    rightForearm = rightElbowJoint.add_child(HierarchyNode("right_forearm"))
    rightForearm.mesh = tubeMesh
    rightForearm.transform = tr.matmul([tr.translate(0, -0.35, 0), tr.scale(0.95, 0.7, 0.95)])
    rightForearm.color = skinColor

    rightHandJoint = rightForearm.add_child(HierarchyNode("right_hand"))
    rightHandJoint.mesh = ballMesh
    rightHandJoint.transform = tr.matmul([tr.translate(0, -0.5, 0), tr.scale(1.2, 0.35, 1.2)])
    rightHandJoint.color = skinColor

    leftHipJoint = trunk.add_child(HierarchyNode("left_hip"))
    leftHipJoint.mesh = ballMesh
    leftHipJoint.transform = tr.matmul([tr.translate(-0.2, -0.55, 0), tr.scale(0.22, 0.22, 0.22)])
    leftHipJoint.color = pantsColor
    leftThigh = leftHipJoint.add_child(HierarchyNode("left_thigh"))
    leftThigh.mesh = tubeMesh
    leftThigh.transform = tr.matmul([tr.translate(0, -0.45, 0), tr.scale(legThickness, 0.9, legThickness)])
    leftThigh.color = pantsColor

    leftKnee = leftThigh.add_child(HierarchyNode("left_knee"))
    leftKnee.mesh = ballMesh
    leftKnee.transform = tr.matmul([tr.translate(0, -0.5, 0), tr.scale(1.2, 0.3, 1.2)])
    leftKnee.color = skinColor

    leftShin = leftKnee.add_child(HierarchyNode("left_shin"))
    leftShin.mesh = tubeMesh
    leftShin.transform = tr.matmul([tr.translate(0, -0.45, 0), tr.scale(0.9, 0.9, 0.9)])
    leftShin.color = pantsColor


    leftFootJoint = leftShin.add_child(HierarchyNode("left_foot"))
    leftFootJoint.mesh = boxMesh
    leftFootJoint.transform = tr.matmul([tr.translate(0, -0.5, 0.1), tr.scale(0.3, 0.2, 0.5)])
    leftFootJoint.color = shoesColor
    rightHipJoint = trunk.add_child(HierarchyNode("right_hip"))
    rightHipJoint.mesh = ballMesh
    rightHipJoint.transform = tr.matmul([tr.translate(0.2, -0.55, 0), tr.scale(0.22, 0.22, 0.22)])
    rightHipJoint.color = pantsColor

    rightThigh = rightHipJoint.add_child(HierarchyNode("right_thigh"))
    rightThigh.mesh = tubeMesh
    rightThigh.transform = tr.matmul([tr.translate(0, -0.45, 0), tr.scale(legThickness, 0.9, legThickness)])
    rightThigh.color = pantsColor
    rightKnee = rightThigh.add_child(HierarchyNode("right_knee"))
    rightKnee.mesh = ballMesh
    rightKnee.transform = tr.matmul([tr.translate(0, -0.5, 0), tr.scale(1.2, 0.3, 1.2)])
    rightKnee.color = skinColor


    rightShin = rightKnee.add_child(HierarchyNode("right_shin"))
    rightShin.mesh = tubeMesh
    rightShin.transform = tr.matmul([tr.translate(0, -0.45, 0), tr.scale(0.9, 0.9, 0.9)])
    rightShin.color = pantsColor

    rightFootJoint = rightShin.add_child(HierarchyNode("right_foot"))
    rightFootJoint.mesh = boxMesh
    rightFootJoint.transform = tr.matmul([tr.translate(0, -0.5, 0.1), tr.scale(0.3, 0.2, 0.5)])
    rightFootJoint.color = shoesColor

    return {
        'root': sceneRoot,
        'torso': trunk,
        'head': headNode,
        'left_shoulder': leftShoulderJoint,
        'left_elbow': leftElbowJoint,
        'left_hand': leftHandJoint,
        'right_shoulder': rightShoulderJoint,
        'right_elbow': rightElbowJoint,
        'right_hand': rightHandJoint,
        'left_hip': leftHipJoint,
        'left_knee': leftKnee,
        'left_foot': leftFootJoint,
        'right_hip': rightHipJoint,
        'right_knee': rightKnee,
        'right_foot': rightFootJoint,
    }


class CharacterPose:
    def __init__(self, name, joint_rotations, camera_config):
        self.name = name
        self.joint_rotations = joint_rotations
        self.camera_config = camera_config



def definePoseSet():
    # Pose 1
    pose1 = CharacterPose(
        name="Postura Intimidante",
        joint_rotations={
            'torso': tr.rotationY(np.pi / 8),
            'head': tr.matmul([tr.translate(0, 0.4, 0), tr.rotationZ(-np.pi / 12), tr.translate(0, -0.4, 0)]),
            'left_shoulder': tr.matmul([tr.translate(0, 0, 0), tr.rotationZ(np.pi / 4), tr.rotationX(np.pi / 6)]),
            'left_elbow': tr.matmul([tr.translate(0, -0.5, 0), tr.rotationZ(np.pi / 3), tr.translate(0, 0.5, 0)]),
            'right_shoulder': tr.matmul([tr.translate(0, 0, 0), tr.rotationZ(-np.pi / 3), tr.rotationX(-np.pi / 4)]),
            'right_elbow': tr.matmul([tr.translate(0, -0.5, 0), tr.rotationZ(-np.pi / 2.5), tr.translate(0, 0.5, 0)]),
            'left_hip': tr.matmul([tr.translate(0, 0, 0), tr.rotationX(np.pi / 8)]),
            'right_hip': tr.matmul([tr.translate(0, 0, 0), tr.rotationX(-np.pi / 12)]),
        },
        camera_config={
            'eye': np.array([3, 1.5, 4], dtype=np.float32),
            'at': np.array([0, 0.5, 0], dtype=np.float32),
            'up': np.array([0, 1, 0], dtype=np.float32)
        }
    )

    # Pose 2
    pose2 = CharacterPose(
        name="Señalando al Futuro",
        joint_rotations={
            'torso': tr.rotationY(-np.pi / 6),
            'head': tr.matmul([tr.translate(0, 0.4, 0), tr.rotationY(np.pi / 6), tr.translate(0, -0.4, 0)]),
            'left_shoulder': tr.matmul([tr.translate(0, 0, 0), tr.rotationZ(np.pi / 6)]),
            'right_shoulder': tr.matmul([tr.translate(0, 0, 0), tr.rotationZ(-np.pi / 2), tr.rotationY(np.pi / 4), tr.rotationX(-np.pi / 8)]),
            'right_elbow': tr.matmul([tr.translate(0, -0.5, 0), tr.rotationZ(-np.pi / 6), tr.translate(0, 0.5, 0)]),

            'left_hip': tr.matmul([tr.translate(0, 0, 0), tr.rotationX(-np.pi / 10), tr.rotationZ(np.pi / 12)]),
            'right_hip': tr.matmul([tr.translate(0, 0, 0), tr.rotationX(np.pi / 6)]),
            'right_knee': tr.matmul([tr.translate(0, -0.5, 0), tr.rotationX(np.pi / 8), tr.translate(0, 0.5, 0)]),
        },
        camera_config={
            'eye': np.array([4, 0.5, 2], dtype=np.float32),
            'at': np.array([0, 1, 0], dtype=np.float32),
            'up': np.array([0, 1, 0], dtype=np.float32)
        }
    )

    # Pose 3 (Bellingham)
    pose3 = CharacterPose(
        name="CelebracionEpica",
        joint_rotations={
            'torso': tr.identity(),
            'head': tr.matmul([tr.translate(0, 0.4, 0), tr.rotationX(np.pi / 8), tr.translate(0, -0.4, 0)]),
            'left_shoulder': tr.matmul([tr.translate(0, 0, 0), tr.rotationZ(np.pi / 2 + np.pi / 12), tr.rotationY(-np.pi / 10)]),
            'left_elbow': tr.matmul([tr.translate(0, -0.5, 0), tr.rotationZ(0), tr.translate(0, 0.5, 0)]),

            'right_shoulder': tr.matmul([tr.translate(0, 0, 0), tr.rotationZ(-np.pi / 2 - np.pi / 12), tr.rotationY(np.pi / 10)]),
            'right_elbow': tr.matmul([tr.translate(0, -0.5, 0), tr.rotationZ(0), tr.translate(0, 0.5, 0)]),
            'left_hip': tr.matmul([tr.translate(0, 0, 0), tr.rotationZ(np.pi / 20)]),
            'right_hip': tr.matmul([tr.translate(0, 0, 0), tr.rotationZ(-np.pi / 20)]),
        },
        camera_config={
            'eye': np.array([0, 0.3, 4.5], dtype=np.float32),
            'at': np.array([0, 1.3, 0], dtype=np.float32),
            'up': np.array([0, 1, 0], dtype=np.float32)
        }
    )

    return [pose1, pose2, pose3]


def setPoseConfiguration(character, pose):
    # Aplica rotaciones del diccionario de la pose
    for joint_name, rotation in pose.joint_rotations.items():
        if joint_name in character:
            joint = character[joint_name]
            base_transform = joint.transform
            joint.transform = tr.matmul([rotation, base_transform])


def resetToBasePosition(character):
    return buildPlayerModel()



class RenderWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Personaje Articulado", resizable=False)
        glClearColor(0.1, 0.1, 0.15, 1.0)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(current_dir, 'vertex_shader.glsl'), 'r') as f:
            vertex_source = f.read()
        with open(os.path.join(current_dir, 'fragment_shader.glsl'), 'r') as f:
            fragment_source = f.read()

        self.renderShader = RenderProgram(vertex_source, fragment_source)

        self.playerModel = buildPlayerModel()


        self.poseLibrary = definePoseSet()
        self.activePoseIdx = 0

        setPoseConfiguration(self.playerModel, self.poseLibrary[self.activePoseIdx])

        self.refreshCameraView()

        self.perspectiveProj = tr.perspective(45, WIDTH / HEIGHT, 0.1, 100)

        print("TAREA 2: PERSONAJE ARTICULADO Y POSES")
        print(f"Pose actual: {self.poseLibrary[self.activePoseIdx].name}")

    def refreshCameraView(self):
        cfg = self.poseLibrary[self.activePoseIdx].camera_config
        self.cameraView = tr.lookAt(cfg['eye'], cfg['at'], cfg['up'])
        self.eyePosition = cfg['eye']


    def handleKeyInput(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.activePoseIdx = (self.activePoseIdx + 1) % len(self.poseLibrary)
            self.playerModel = buildPlayerModel()
            setPoseConfiguration(self.playerModel, self.poseLibrary[self.activePoseIdx])
            self.refreshCameraView()
            print(f"Pose cambiada a: {self.poseLibrary[self.activePoseIdx].name}")
        elif symbol == key.ESCAPE:
            self.close()

    # pyglet event binding uses original names; keep them but forward
    def on_key_press(self, symbol, modifiers):
        return self.handleKeyInput(symbol, modifiers)


    def renderScene(self):
        self.clear()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.renderShader.useProgram()
        program = self.renderShader.getProgramID()

        glUniformMatrix4fv(glGetUniformLocation(program, "view"), 1, GL_TRUE, self.cameraView)
        glUniformMatrix4fv(glGetUniformLocation(program, "projection"), 1, GL_TRUE, self.perspectiveProj)

        glUniform3f(glGetUniformLocation(program, "lightPos"), 5.0, 5.0, 5.0)
        glUniform3f(glGetUniformLocation(program, "viewPos"), self.eyePosition[0], self.eyePosition[1], self.eyePosition[2])

        self.playerModel['root'].draw(program)
        self.renderFloor(program)


    # forward for pyglet
    def on_draw(self):
        return self.renderScene()

    def renderFloor(self, program):
        if not hasattr(self, 'floorPlane'):
            from .geometry import Mesh
            vertices = np.array([-5, -2.5, -5, 5, -2.5, -5, 5, -2.5, 5, -5, -2.5, 5], dtype=np.float32)
            indices = np.array([0,1,2,2,3,0], dtype=np.uint32)
            self.floorPlane = Mesh(vertices, indices)


        glUniformMatrix4fv(glGetUniformLocation(program, "model"), 1, GL_TRUE, tr.identity())
        glUniform3f(glGetUniformLocation(program, "color"), 0.15, 0.15, 0.2)
        self.floorPlane.draw()


def main():
    win = RenderWindow()
    pyglet.app.run()


if __name__ == "__main__":
    main()
