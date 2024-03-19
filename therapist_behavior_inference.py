import argparse

from utils_mistral import *

intent_detail_list = read_prompt_csv('therapist')
def get_therapist_intent(utterance,context):
	utterance = str(utterance).strip()
	context = str(context).strip()
	messages = create_message_therapist(intent_detail_list, utterance,context)
	response = get_completion_from_messages_local(messages, temperature=0.7)

	return response


parser = argparse.ArgumentParser(description='Behavior Inference')

parser.add_argument('--input_path', type=str, default='dataset/sample_therapist_input.jsonl', help='Path to input')
parser.add_argument('--output_path', type=str, default='dataset/sample_therapist_output.jsonl', help='Path to output')

args = parser.parse_args()


input_path = args.input_path
output_path = args.output_path


print('Input Path: ', input_path)
print('Output Path: ', output_path)

	
f = codecs.open(input_path, 'r', 'utf-8')
output_f = codecs.open(output_path, 'w', 'utf-8')

for row in tqdm(f):
	curr_json = json.loads(row.strip())

	curr_json['intent'] = get_therapist_intent(curr_json['Utterance'], curr_json['context'])
	print(json.dumps(curr_json), file=output_f)

f.close()
output_f.close()