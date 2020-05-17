def Create3dHtml(export_file_name:str):
    from pythreejs import Mesh, BoxBufferGeometry, MeshLambertMaterial,\
        CombinedCamera, PointLight, AmbientLight, OrbitControls, Scene,\
        Renderer
    from ipywidgets import embed
    from IPython.display import display

    base = Mesh(
        BoxBufferGeometry(20, 0.1, 20), 
        MeshLambertMaterial(color='green', opacity=0.5, transparent=True),
        position=(0, 0, 0),
    )
    cube = Mesh(
        BoxBufferGeometry(10, 10, 10), 
        MeshLambertMaterial(color='red', opacity=0.5, transparent=False),
        position=(0, 5, 0),
    )
    target = (0, 5, 0)
    view_width = 600
    view_height = 400
    camera = CombinedCamera(position=[60, 60, 60], width=view_width, height=view_height)
    camera.mode = 'orthographic'
    lights = [
        PointLight(position=[100, 0, 0], color="#ffffff"),
        PointLight(position=[0, 100, 0], color="#bbbbbb"),
        PointLight(position=[0, 0, 100], color="#888888"),
        AmbientLight(intensity=0.2),
    ]
    orbit = OrbitControls(controlling=camera, target=target)
    camera.lookAt(target)
    scene = Scene(children=[base, cube, camera] + lights)
    renderer = Renderer(scene=scene, camera=camera, controls=[orbit],
                        width=view_width, height=view_height)
    camera.zoom = 4
    
    # TODO - Can use embed.embed_snippet, into another html
    embed.embed_minimal_html(export_file_name, views=renderer, title='Renderer')
    display(renderer)
    return

def Get3dSnippet():
    from pythreejs import Mesh, BoxBufferGeometry, MeshLambertMaterial,\
        CombinedCamera, PointLight, AmbientLight, OrbitControls, Scene,\
        Renderer
    from ipywidgets import embed
    from IPython.display import display

    base = Mesh(
        BoxBufferGeometry(20, 0.1, 20), 
        MeshLambertMaterial(color='green', opacity=0.5, transparent=True),
        position=(0, 0, 0),
    )
    cube = Mesh(
        BoxBufferGeometry(10, 10, 10), 
        MeshLambertMaterial(color='red', opacity=0.5, transparent=False),
        position=(0, 5, 0),
    )
    target = (0, 5, 0)
    view_width = 600
    view_height = 400
    camera = CombinedCamera(position=[60, 60, 60], width=view_width, height=view_height)
    camera.mode = 'orthographic'
    lights = [
        PointLight(position=[100, 0, 0], color="#ffffff"),
        PointLight(position=[0, 100, 0], color="#bbbbbb"),
        PointLight(position=[0, 0, 100], color="#888888"),
        AmbientLight(intensity=0.2),
    ]
    orbit = OrbitControls(controlling=camera, target=target)
    camera.lookAt(target)
    scene = Scene(children=[base, cube, camera] + lights)
    renderer = Renderer(scene=scene, camera=camera, controls=[orbit],
                        width=view_width, height=view_height)
    camera.zoom = 4
    
    snippet = embed.embed_snippet(views=renderer)
    display(renderer)
    return snippet
