TRAIN_FILE = 'generating_queries/training_queries_baseline.pickle'
TEST_FILE = 'generating_queries/test_queries_baseline.pickle'

def get_queries_dict(filename):
	#key:{'query':file,'positives':[files],'negatives:[files], 'neighbors':[keys]}
	with open(filename, 'rb') as handle:
		queries = pickle.load(handle)
		print("Queries Loaded.")
		return queries
		
TRAINING_QUERIES= get_queries_dict(TRAIN_FILE)
TEST_QUERIES= get_queries_dict(TEST_FILE)

train_file_idxs = np.arange(0, len(TRAINING_QUERIES.keys()))

np.random.shuffle(train_file_idxs)


def get_query_tuple():
	#read the query image and pointcloud into numpy
	
	#select and read positive from positive table
	
	#select and read negative from negative table
	
	return query positive negative
	
	 

for i in range(len(train_file_idxs)//BATCH_NUM_QUERIES):
	batch_keys= train_file_idxs[i*BATCH_NUM_QUERIES:(i+1)*BATCH_NUM_QUERIES]
	q_tuples=[]
	q_tuples.append(get_query_tuple(TRAINING_QUERIES[batch_keys[j]],POSITIVES_PER_QUERY,NEGATIVES_PER_QUERY, TRAINING_QUERIES, hard_neg=[], other_neg=True))
	queries=[]
	positives=[]
	negatives=[]
	other_neg=[]

for k in range(len(q_tuples)):
	queries.append(q_tuples[k][0])
	positives.append(q_tuples[k][1])
	negatives.append(q_tuples[k][2])
	other_neg.append(q_tuples[k][3])
	
	feed_dict={ops['query']:queries, ops['positives']:positives, ops['negatives']:negatives, ops['other_negatives']:other_neg, ops['is_training_pl']:is_training, ops['epoch_num']:epoch}
	summary, step, train, loss_val = sess.run([ops['merged'], ops['step'],ops['train_op'], ops['loss']], feed_dict=feed_dict)
	train_writer.add_summary(summary, step)
	log_string('batch loss: %f' % loss_val)	