using CommunityToolkit.Mvvm.ComponentModel;

namespace SharpBoard.ViewModels;

public partial class MainViewModel : ViewModelBase
{
    [ObservableProperty]
    private string _greeting = "Hello, World!";
}