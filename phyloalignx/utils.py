
import subprocess

def run_mafft(input_file, output_file):
    """Run MAFFT for multiple sequence alignment."""
    cmd = f"mafft --auto {input_file} > {output_file}"
    subprocess.run(cmd, shell=True, check=True)
    print(f"MSA completed: {output_file}")

def run_raxml(aligned_file, tree_output, model, bootstrap):
    """Run RAxML to generate a phylogenetic tree."""
    cmd = f"raxmlHPC -s {aligned_file} -n {tree_output} -m {model} -# {bootstrap} -p 12345"
    subprocess.run(cmd, shell=True, check=True)
    print(f"RAxML tree generation completed: {tree_output}")
    