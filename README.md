# MI Dialog act classification

This code is inspired from the following publication:
```bash
@inproceedings{chiu2024bolt,
    title={A Computational Framework for Behavioral Assessment of LLM Therapists},
    author={Chiu, Yu Ying and Sharma, Ashish and Lin, Inna Wanyin and Althoff, Tim},
    journal={arXiv preprint arXiv:2401.00820},
    year={2024}
}
```

## Quickstart

### Create data

The HOPE dataset can be downloaded from : https://github.com/LCS2-IIITD/SPARTA_WSDM2022/tree/main
The data can then be formatted using the create_sata notebook

###  Run Therapist Behavior Inference
```
python therapist_behavior_inference.py --input_path dataset/sample_therapist_input.jsonl --output_path dataset/sample_therapist_output.jsonl
```

The output file will be saved at the path specified by `--output_path`. The output file will contain the `therapist_behavior` field, which contains the inferred therapist behaviors for each utterance.


### Run Client Behavior Inference

```
python client_behavior_inference.py --input_path dataset/sample_client_input.jsonl --output_path dataset/sample_client_output.jsonl
```

The output file will be saved at the path specified by `--output_path`. The output file will contain the `client_behavior` field, which contains the inferred client behaviors for each utterance.

### Annotations

The realized annotations are available in the annotations folder.
The annotations are performed on the test set of the HOPE dataset.
The correspondance between the coding and the dialog acts is availble in the prompt folder.