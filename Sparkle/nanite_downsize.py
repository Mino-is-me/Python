import unreal 
from Lib import __lib_topaz__ as topaz


desired_triangle_percentage : float # UI Binded Value 

assets = topaz.get_selected_assets()
## execution here ##
for each in assets :
    if each.__class__ == unreal.Blueprint : 
        comps = topaz.get_component_by_class(each, unreal.StaticMeshComponent)
        for comp in comps :
            static_mesh     : unreal.StaticMesh                 = comp.static_mesh
            if static_mesh is not None : 

                

                nanite_settings : unreal.MeshNaniteSettings     = static_mesh.get_editor_property('nanite_settings')
                nanite_settings.enabled = True
                nanite_settings.keep_percent_triangles = desired_triangle_percentage 
                static_mesh.set_editor_property('nanite_settings', nanite_settings)
            #print(nanite_settings.keep_percent_triangles)
                
    if each.__class__ == unreal.StaticMesh : 
        if each is not None : 

            nanite_settings : unreal.MeshNaniteSettings     = each.get_editor_property('nanite_settings')
            nanite_settings.enabled = True
            nanite_settings.set_editor_property('keep_percent_triangles', desired_triangle_percentage) 
            each.set_editor_property('nanite_settings', nanite_settings)


 
print('OK')