from docx import Document
import csv

'''
    提取word 层次化结构的知识
'''

def extract_hierarchy(doc_path):
    doc = Document(doc_path)
    hierarchy = []
    current_level = [hierarchy]

    for para in doc.paragraphs:
        if para.style.name.startswith('Heading'):
            level = int(para.style.name.split()[1])
            while len(current_level) > level:
                current_level.pop()
            current_hierarchy = {'title': para.text, 'level': level, 'subsections': []}
            current_level[-1].append(current_hierarchy)
            current_level.append(current_hierarchy['subsections'])
        else:
            if len(current_level) > 1:
                current_level[-1].append({'content': para.text, 'level': current_level[-2][-1]['level'] + 1})

    return hierarchy

def flatten_hierarchy(hierarchy, level_titles=None, parent_titles=None):
    if level_titles is None:
        level_titles = []
    if parent_titles is None:
        parent_titles = []

    rows = []
    for item in hierarchy:
        if 'title' in item:
            current_titles = parent_titles + [item['title']]
            row = current_titles + [''] * (len(level_titles) - len(current_titles))
            rows.append(row)
            rows.extend(flatten_hierarchy(item['subsections'], level_titles, current_titles))
        else:
            current_titles = parent_titles + [item['content']]
            row = current_titles + [''] * (len(level_titles) - len(current_titles))
            rows.append(row)
    return rows

def save_to_csv(hierarchy, csv_path):
    level_titles = ['Level 1', 'Level 2', 'Level 3', 'Level 4', 'Level 5', 'Content']
    rows = flatten_hierarchy(hierarchy, level_titles)
    with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(level_titles)
        for row in rows:
            writer.writerow(row)


# 文档路径
doc_path = 'data/信息技术与数据挖掘-2021-8-16.docx'
csv_path = 'output_data/output.csv'

hierarchy = extract_hierarchy(doc_path)
save_to_csv(hierarchy, csv_path)

