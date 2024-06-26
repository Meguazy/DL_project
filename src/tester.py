import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms

from model_class import CustomCNN
from torch.utils.data import DataLoader

tr_transf = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomVerticalFlip(p=0.5),
    transforms.ToTensor()])

# Initialize the model
model = CustomCNN(1)

# Load the state dictionary from the .pth file
state_dict = torch.load('./model/cnn.pth')

# Load the state dictionary into the model
model.load_state_dict(state_dict)

# Load the test set
test_set = torchvision.datasets.ImageFolder(r'archive/casting_data/casting_data/test/', transform=tr_transf)
test_loader = DataLoader(test_set, batch_size=32, shuffle=True)

# Loss function
criterion = nn.BCELoss()

# Validate the model on the test set
test_acc, test_loss, test_f1 = model.validate(test_loader, model, criterion)

# Print the results of the test set validation
print(f'Test Accuracy: {test_acc}')
print(f'Test Loss: {test_loss}')
print(f'Test F1 Score: {test_f1}')
