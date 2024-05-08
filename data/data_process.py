import json

# 读取原始数据文件
def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

# 转换数据格式
def convert_to_sharegpt_format(original_data):
    new_data = []
    for item in original_data:
        new_item = {}
        new_item['conversations'] = []
        new_item['system'] = item['conversation'][0]['system']
        new_item['tools'] = ""
        for dialog in item['conversation']:
            new_item['conversations'].append({
                "from": "human",
                "value": dialog.get('input', '')
            })
            new_item['conversations'].append({
                "from": "gpt",
                "value": dialog.get('output', '')
            })
        new_data.append(new_item)
    return new_data

# 写数据到新的JSON文件
def save_data(new_data, output_filepath):
    with open(output_filepath, 'w', encoding='utf-8') as file:
        json.dump(new_data, file, indent=4, ensure_ascii=False)

# 主函数
def main():
    input_filepath = 'data_pro.json'
    output_filepath = 'converted_data.json'
    original_data = load_data(input_filepath)
    converted_data = convert_to_sharegpt_format(original_data)
    save_data(converted_data, output_filepath)

if __name__ == "__main__":
    main()
    print("done")
