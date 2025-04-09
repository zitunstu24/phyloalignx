import os
import yaml
import argparse
from utils import run_mafft
from utils import run_raxml

def load_config(config_file):
    """Load YAML configuration file."""
    with open(os.path.join("config", config_file), 'r') as file:
        return yaml.safe_load(file)


def main(config_path):
    config = load_config(config_path) 
    input_seq = config['input_sequence_file']
    aligned_output = config['aligned_output_file']
    tree_output = config['tree_output_file']
    model = config.get('raxml_model')
    bootstrap = config.get('bootstrap_replicates')
    
    # Run MAFFT
    run_mafft(input_seq, aligned_output)
    
    # Run RAxML
    run_raxml(aligned_output, tree_output, model, bootstrap)
    print("Pipeline execution complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run MSA and RAxML pipeline")
    parser.add_argument('--config', type=str, required=True, help='Path to config file (inside config folder)')
    args = parser.parse_args()
    main(args.config)
