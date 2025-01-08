import yaml

def read_convention(lpgbt_nb, module_nb):
    yaml_file_path = 'config/convention_table.yaml'

    with open(yaml_file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)

    target_lpgbt = lpgbt_nb
    target_module = module_nb

    # print(f"target_lpgbt: {target_lpgbt}, target_module: {target_module}")

    result = None
    for lpgbt in data['Lpgbts']:
        if lpgbt['lpgbt'] == target_lpgbt:
            for module in lpgbt['Modules']:
                if module['module'] == target_module:
                    result = module
                    break
        if result:
            break

    if result:
        return result
    else:
        return 0