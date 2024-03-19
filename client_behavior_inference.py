import argparse

from utils_mistral import *

intent_detail_list = read_prompt_csv('client')
# export API key to environment variable
def get_client_intent(utterance,context):
	utterance = utterance.strip()
	context = context.strip()
	messages = create_message_client(intent_detail_list, utterance,context)
	response = get_completion_from_messages_local(messages, temperature=0.7)


	return response


parser = argparse.ArgumentParser(description='Behavior Inference')

parser.add_argument('--input_path', type=str, default='dataset/sample_client_input.jsonl', help='Path to input')
parser.add_argument('--output_path', type=str, default='dataset/sample_client_output.jsonl', help='Path to output')
args = parser.parse_args()

input_path = args.input_path
output_path = args.output_path


print('Input Path: ', input_path)
print('Output Path: ', output_path)
f = codecs.open(input_path, 'r', 'utf-8')
output_f = codecs.open(output_path, 'w', 'utf-8')

for row in tqdm(f):
	curr_json = json.loads(row.strip())


	curr_json['intent'] = get_client_intent(curr_json['Utterance'],curr_json['context'])
	print(json.dumps(curr_json), file=output_f)

f.close()
output_f.close()