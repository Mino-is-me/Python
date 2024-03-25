import unreal
import importlib
from Lib import __lib_topaz__ as topaz
from Lib import __lib_stelle__ as stelle
importlib.reload(topaz)
importlib.reload(stelle)


def assetValidator(folder_path : str) -> list[str] : #Returns a list of assets that are too long
    need_to_return = []
    assets = topaz.get_assets_in_folder(folder_path)
    for asset in assets:
        file_len = len(asset)
        if file_len > 235 :
            need_to_return.append(asset)
            print('Asset Name : ' + asset + ' is too long. Please rename it.' + ' Length : ' + str(file_len) )
    return need_to_return

def bulk_renamer(asset_path_list : str) -> None:
    for i in asset_path_list:
        #print(i)
        if '_BaseColor' in i:
            newName = i.replace('_BaseColor','_D')
        elif '_Normal' in i:
            newName = i.replace('_Normal','_N')
        elif '_OcclusionRoughnessMetallic' in i:
            newName = i.replace('_OcclusionRoughnessMetallic','_ORM')
        else:
            newName = i
        unreal.EditorAssetLibrary.rename_asset(i,newName)
        print('Renamed ' + i + ' to ' + newName)

def spine_breaker(asset : unreal.Object) -> None:
    topaz.set_texture_size_by_bound(topaz.get_actor_bound_size(topaz.get_asset_from_static_mesh_actor(asset)),topaz.get_textures_list_from_materials(asset.get_editor_property('materials')))

#spine_breaker(topaz.get_selected_asset())

#bulk_renamer(shit_list)
#stelle.write_list_to_csv(shit_list, r'D:/art_Narr_SpicePro/CINEVStudio/Content/Python/Debug')
###Initialised message when loaded ###
unreal.log('archeron initialised...')



