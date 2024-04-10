

# Train the model
history = model.fit(train_generator, epochs=10, validation_data=validation_generator)

# Use the trained model to predict labels for test images
predictions = model.predict(test_images)