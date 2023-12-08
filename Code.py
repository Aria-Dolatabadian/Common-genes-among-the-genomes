import csv
def read_genes_from_csv(file_path):
    genes = set()
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            gene_info = (
                row['Gene Name'],
                int(row['Chromosome Number']),
                int(row['Start']),
                int(row['End']),

                row['Type']
            )
            genes.add(gene_info)
    return genes

def compare_genes(file1, file2, file3):
    genes_individual1 = read_genes_from_csv(file1)
    genes_individual2 = read_genes_from_csv(file2)
    genes_individual3 = read_genes_from_csv(file3)

    genes_common_1_2 = genes_individual1.intersection(genes_individual2)
    genes_common_1_3 = genes_individual1.intersection(genes_individual3)
    genes_common_2_3 = genes_individual2.intersection(genes_individual3)
    genes_common_1_2_3 = genes_individual1.intersection(genes_individual2, genes_individual3)

    # Exclude genes common in all three genomes from two-by-two comparisons
    genes_common_1_2 = genes_common_1_2.difference(genes_common_1_2_3)
    genes_common_1_3 = genes_common_1_3.difference(genes_common_1_2_3)
    genes_common_2_3 = genes_common_2_3.difference(genes_common_1_2_3)

    return genes_common_1_2, genes_common_1_3, genes_common_2_3, genes_common_1_2_3

def export_common_genes_to_csv(genes_common_1_2, genes_common_1_3, genes_common_2_3, genes_common_1_2_3, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Gene Name', 'Chromosome Number', 'Start', 'End', 'Type', 'Genomes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for gene in genes_common_1_2:
            gene_dict = {
                'Gene Name': gene[0],
                'Chromosome Number': gene[1],
                'Start': gene[2],
                'End': gene[3],
                'Type': gene[4],
                'Genomes': '1 and 2'
            }
            writer.writerow(gene_dict)

        for gene in genes_common_1_3:
            gene_dict = {
                'Gene Name': gene[0],
                'Chromosome Number': gene[1],
                'Start': gene[2],
                'End': gene[3],
                'Type': gene[4],
                'Genomes': '1 and 3'
            }
            writer.writerow(gene_dict)

        for gene in genes_common_2_3:
            gene_dict = {
                'Gene Name': gene[0],
                'Chromosome Number': gene[1],
                'Start': gene[2],
                'End': gene[3],
                'Type': gene[4],
                'Genomes': '2 and 3'
            }
            writer.writerow(gene_dict)

        for gene in genes_common_1_2_3:
            gene_dict = {
                'Gene Name': gene[0],
                'Chromosome Number': gene[1],
                'Start': gene[2],
                'End': gene[3],
                'Type': gene[4],
                'Genomes': '1 and 2 and 3'
            }
            writer.writerow(gene_dict)

file_path_individual1 = 'individual1_genome.csv'
file_path_individual2 = 'individual2_genome.csv'
file_path_individual3 = 'individual3_genome.csv'
output_file_path = 'common_genes_among_the_genomes.csv'

genes_common_1_2, genes_common_1_3, genes_common_2_3, genes_common_1_2_3 = compare_genes(file_path_individual1, file_path_individual2, file_path_individual3)
export_common_genes_to_csv(genes_common_1_2, genes_common_1_3, genes_common_2_3, genes_common_1_2_3, output_file_path)

print(f"Common genes among {file_path_individual1}, {file_path_individual2}, and {file_path_individual3} exported to {output_file_path}.")
