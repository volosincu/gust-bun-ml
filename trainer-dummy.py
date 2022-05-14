


# model = TextGenModel(
#     vocab_size=vocab_size,
#     embedding_dim=embedding_dim,
#     rnn_units=rnn_units)

# for input_example_batch, target_example_batch in dataset.take(1):
#     example_batch_predictions = model(input_example_batch)
#     print(example_batch_predictions.shape, "# (batch_size, sequence_length, vocab_size)")

# model.summary()
# sampled_indices = tf.random.categorical(example_batch_predictions[0], num_samples=1)
# sampled_indices = tf.squeeze(sampled_indices, axis=-1).numpy()

# print(input_example_batch[0])

# print("Input:\n", text_from_ids(input_example_batch[0]).numpy())
# print()
# print("Next Char Predictions:\n", text_from_ids(sampled_indices).numpy())

# loss = tf.losses.SparseCategoricalCrossentropy(from_logits=True)
# example_batch_mean_loss = loss(target_example_batch, example_batch_predictions)
# print("Prediction shape: ", example_batch_predictions.shape, " # (batch_size, sequence_length, vocab_size)")
# print("Mean loss:        ", example_batch_mean_loss)


# tf.exp(example_batch_mean_loss).numpy()
# model.compile(optimizer='adam', loss=loss)


# # Directory where the checkpoints will be saved
# checkpoint_dir = './training_checkpoints'
# # Name of the checkpoint files
# checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt_{epoch}")

# checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
#     filepath=checkpoint_prefix,
#     save_weights_only=True)





## TRAIN 
# EPOCHS = 1
# history = model.fit(dataset, epochs=EPOCHS, callbacks=[checkpoint_callback])

###############################################################################



# one_step_model = OneStep(model, chars_from_ids, ids_from_chars)


# # SAVE Model 
# tf.saved_model.save(one_step_model, 'model-rețete-v1')



# start = time.time()
# states = None
# next_char = tf.constant(['Leurda'])
# result = [next_char]

# for n in range(1000):
#   next_char, states = one_step_model.generate_one_step(next_char, states=states)
#   result.append(next_char)

# result = tf.strings.join(result)
# end = time.time()
# print(result[0].numpy().decode('utf-8'), '\n\n' + '_'*80)
# print('\nRun time:', end - start)
