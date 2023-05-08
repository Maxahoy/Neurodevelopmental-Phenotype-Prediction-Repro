import torch
import torch.nn.functional as F

def train_model(train_loader, model, optimizer):
    model.train()
    train_accs = []
    for train_data in train_loader:
        optimizer.zero_grad()
        x, y_true = train_data
        x = x.to(model.device)
        y_true = y_true.to(model.device)
        y_pred = model(x)
        train_loss = F.mse_loss(y_pred, y_true)
        train_loss.backward()
        optimizer.step()
        train_acc = F.l1_loss(y_pred, y_true)
        train_accs.append(train_acc)
    return sum(train_accs) / len(train_accs)

def test_model(test_loader, model):
    model.eval()
    test_accs = []
    with torch.no_grad():
        for test_data in test_loader:
            x, y_true = test_data
            x = x.to(model.device)
            y_true = y_true.to(model.device)
            y_pred = model(x)
            test_acc = F.l1_loss(y_pred, y_true)
            test_accs.append(test_acc)
    return sum(test_accs) / len(test_accs)

def display_test_stats(test_loader, model):
    model.eval()
    test_accs = []
    print("This ran")
    predictions = []
    truths = []
    with torch.no_grad():
        for test_data in test_loader:
            x, y_true = test_data
            truths.append(y_true)
            x = x.to(model.device)
            y_true = y_true.to(model.device)
            y_pred = model(x) #todo; see what this is predicting by usinjg printouts, can it predict a class 1 or 0?
            # can another one be trained to try and predict birth sex?
            #print('y_pred', y_pred)
            predictions.append(y_pred)
            


            #predictions.append(y_pred)
            

            test_acc = F.l1_loss(y_pred, y_true) #gets the mean element-wise absolute value difference;
            # this 
            test_accs.append(test_acc)
    #stats we want; average accuracy (sum of accs / len of accs)

    #we want to update this code so that it spits back the accuracy of the scanned ages and birth ages
    #
    # 
    mae = F.l1_loss(y_pred, y_true)
    return (sum(test_accs) / len(test_accs)), predictions, truths, mae


