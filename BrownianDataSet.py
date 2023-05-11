import numpy as np, matplotlib.pyplot as plt, random as r

def brownian_motion(n, width, height):
	x = np.zeros((n+1, 2))
	for i in range(1, n+1):
		# generate random step
		step = np.random.randn(2)
		# normalize step to have length 1
		step /= np.sqrt(np.sum(step**2))
		# update position
		x[i,:] = x[i-1,:] + step
		# ensure point stays within bounds
		x[i,0], x[i,1] = np.clip(x[i,0], 0, width-1), np.clip(x[i,1], 0, height-1)
	return x[1:]

# Generate Brownian motion datasets

n_images, n_points, width, height, brownian_sets = 40, 6000, 60, 60, []

for i in range(n_images):
	brownian_set = brownian_motion(n_points, width, height); brownian_sets.append(brownian_set)

# Create images from Brownian motion datasets
images = []
for brownian_set in brownian_sets:
	img = np.zeros((height, width, 3))
	start_color, end_color = np.array([1.0, 0.0, 0.0]), np.array([0.0, 0.0, 1.0])
	for i in range(n_points):
		x_id, y_id = int(np.round(brownian_set[i, 0])), int(np.round(brownian_set[i, 1]))
		t = i / (n_points - 1)
		color = (1 - t) * start_color + t * end_color
		img[y_id, x_id] = color
	images.append(img)

r.shuffle(images)

# Plot Images
fig, axs = plt.subplots(5, 8, figsize=(12, 12))
for id, ax in enumerate(axs.flatten()): ax.imshow(images[id]); ax.axis('off')

plt.show()
