from torch import nn
import torch
import timm
class VerboseExe:
    def __init__(self, model: nn.Module) -> None:
        self.model = model
        self.handles = []
        
        for name, module in self.model.named_children():
            module.__name__ = name
            self.handles.append(
                module.register_forward_hook(
                    lambda m, _, o: print(
                        f'{m.__name__:10}\t\t\t{o.shape}'
                    ) 
                )
            )
                
    def __call__(self, X) -> None:
        self.model(X)
        for i in range(len(self.handles)):
            self.handles[i].remove()

if __name__ == "__main__":
    model:nn.Module = timm.create_model('resnet18',pretrained= False)
    # model.fc = nn.Linear(2048,31)
    ver = VerboseExe(model)
    x = torch.rand((128,3,224,224))
    # print(model.conv1)
    ver(x)