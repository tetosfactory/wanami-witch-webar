import bpy, sys, os, json, tempfile, zipfile, struct
from mathutils import Vector

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
source = os.path.join(root, 'assets', 'witch.glb')
assets = os.path.join(root, 'assets')
os.makedirs(assets, exist_ok=True)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=source)
meshes = [o for o in bpy.context.scene.objects if o.type == 'MESH']
points = [o.matrix_world @ Vector(c) for o in meshes for c in o.bound_box]
low = Vector([min(p[i] for p in points) for i in range(3)])
high = Vector([max(p[i] for p in points) for i in range(3)])
factor = 1.0 / (high.z-low.z)
center = Vector(((low.x+high.x)/2, (low.y+high.y)/2, low.z))
# Bake world transforms and normalize to a 1 m tall model standing on Z=0.
for o in meshes:
    world = o.matrix_world.copy()
    o.parent = None
    o.matrix_world.identity()
    for v in o.data.vertices:
        v.co = (world @ v.co - center) * factor
    o.data.update()
    bpy.context.view_layer.objects.active = o
    if len(o.data.polygons) > 60000:
        modifier = o.modifiers.new('Mobile geometry', 'DECIMATE')
        modifier.ratio = 60000 / len(o.data.polygons)
        bpy.ops.object.modifier_apply(modifier=modifier.name)
for image in bpy.data.images:
    if image.size[0] > 0 and max(image.size) > 1024:
        scale = 1024 / max(image.size)
        image.scale(round(image.size[0]*scale), round(image.size[1]*scale))
        image.pack()
bpy.ops.object.select_all(action='DESELECT')
for o in meshes: o.select_set(True)
bpy.ops.export_scene.gltf(filepath=os.path.join(assets, 'witch-mobile.glb'), use_selection=True,
    export_format='GLB', export_image_format='AUTO', export_animations=False)
# Package PNG textures for Quick Look. USD export can otherwise emit generated EXR images.
work = os.path.join(os.path.dirname(os.path.dirname(root)), 'work')
os.makedirs(work, exist_ok=True)
with tempfile.TemporaryDirectory(prefix='witch-usd-', dir=work) as usd_dir:
    usd_path = os.path.join(usd_dir, 'witch.usda')
    bpy.ops.wm.usd_export(filepath=usd_path, selected_objects_only=True,
        export_animation=False, export_materials=True, export_textures_mode='NEW',
        generate_preview_surface=True, generate_materialx_network=False,
        export_custom_properties=False, convert_orientation=True,
        export_global_forward_selection='NEGATIVE_Z', export_global_up_selection='Y',
        meters_per_unit=1.0)
    with open(usd_path, encoding='utf-8') as handle: usd_text = handle.read()
    for directory, _, files in os.walk(usd_dir):
        for name in files:
            if name.lower().endswith('.exr'):
                image = bpy.data.images.load(os.path.join(directory, name), check_existing=False)
                _ = image.pixels[0]
                image.file_format = 'PNG'
                image.filepath_raw = os.path.join(directory, name[:-4]+'.png')
                image.save()
                usd_text = usd_text.replace(name, name[:-4]+'.png')
    with open(usd_path, 'w', encoding='utf-8') as handle: handle.write(usd_text)
    members = [('witch.usda', usd_path)]
    for directory, _, files in os.walk(usd_dir):
        for name in sorted(files):
            if name.lower().endswith(('.png', '.jpg', '.jpeg')):
                filename = os.path.join(directory, name)
                members.append((os.path.relpath(filename, usd_dir).replace(os.sep, '/'), filename))
    with zipfile.ZipFile(os.path.join(assets, 'witch.usdz'), 'w', compression=zipfile.ZIP_STORED) as archive:
        for name, filename in members:
            info = zipfile.ZipInfo(name)
            padding = (-((archive.fp.tell()) + 30 + len(name.encode('utf-8')))) % 64
            if padding and padding < 4: padding += 64
            if padding: info.extra = struct.pack('<HH', 0xffff, padding-4) + bytes(padding-4)
            with open(filename, 'rb') as handle: archive.writestr(info, handle.read())
scene = bpy.context.scene
scene.render.engine='CYCLES'
scene.cycles.samples=16
scene.render.resolution_x=800
scene.render.resolution_y=900
scene.render.resolution_percentage=100
scene.render.film_transparent=True
scene.world.color=(0.35,0.35,0.35)
bpy.ops.object.camera_add(location=(0,-2.8,1.0))
camera=bpy.context.object
camera.rotation_euler=(Vector((0,0,0.5))-camera.location).to_track_quat('-Z','Y').to_euler()
camera.data.type='ORTHO'
camera.data.ortho_scale=1.45
scene.camera=camera
for location, energy, size in [((2,-3,4),450,4),((-2,-1,2),250,3),((0,2,3),400,3)]:
    bpy.ops.object.light_add(type='AREA', location=location)
    lamp=bpy.context.object
    lamp.data.energy=energy
    lamp.data.shape='DISK'
    lamp.data.size=size
    lamp.rotation_euler=(Vector((0,0,0.5))-lamp.location).to_track_quat('-Z','Y').to_euler()
scene.render.filepath=os.path.join(assets,'witch-poster.png')
bpy.ops.render.render(write_still=True)
report={'source_bytes':os.path.getsize(source), 'height_m':1.0,
 'meshes':len(meshes), 'triangles':sum(len(o.data.polygons) for o in meshes),
 'glb_bytes':os.path.getsize(os.path.join(assets,'witch-mobile.glb')),
 'usdz_bytes':os.path.getsize(os.path.join(assets,'witch.usdz'))}
with open(os.path.join(root,'model-report.json'),'w',encoding='utf-8') as f: json.dump(report,f,indent=2)
print('MODEL_READY',json.dumps(report))
