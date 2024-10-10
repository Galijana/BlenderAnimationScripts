import bpy

# Brisanje svih postojećih objekata
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Kreiranje kocke
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))

# Pomeranje kocke na drugu poziciju
kocka = bpy.context.object
kocka.location.x += 2
kocka.location.y += 2
kocka.location.z += 2

# Dodaj kuglu
bpy.ops.mesh.primitive_uv_sphere_add(location=(0, 0, 0))

# Rotacija kugle
kugla = bpy.context.object
kugla.rotation_euler[0] += 1.57  # Rotacija za 90 stepeni oko X ose

# Pomeranje kugle
kugla.location.x += 3
kugla.location.y += 3

# Dodaj cilindar
bpy.ops.mesh.primitive_cylinder_add(location=(-2, -2, 0))

# Skaliraj cilindar
cilindar = bpy.context.object
cilindar.scale.x = 0.5  # Skaliranje po X osi
cilindar.scale.y = 0.5  # Skaliranje po Y osi
cilindar.scale.z = 2    # Skaliranje po Z osi

# Animacija kocke - rotacija kroz 100 frejmova
kocka.rotation_euler = (0, 0, 0)
kocka.keyframe_insert(data_path="rotation_euler", frame=1)

kocka.rotation_euler = (0, 0, 3.14159)
kocka.keyframe_insert(data_path="rotation_euler", frame=100)

# Animacija kugle - pomeranje kroz 100 frejmova
kugla.location = (0, 0, 0)
kugla.keyframe_insert(data_path="location", frame=1)

kugla.location = (5, 0, 0)
kugla.keyframe_insert(data_path="location", frame=100)
