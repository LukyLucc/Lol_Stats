from Wrapper import *
from Plotter import *

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sampel_matches = ['EUW1_5675455489', 'EUW1_5675378816', 'EUW1_5675402656', 'EUW1_5673282942', 'EUW1_5669648539', 'EUW1_5669620635', 'EUW1_5667456956', 'EUW1_5665085560', 'EUW1_5665080642', 'EUW1_5663575630', 'EUW1_5663433898', 'EUW1_5661622687', 'EUW1_5661583090', 'EUW1_5659070171', 'EUW1_5652489617', 'EUW1_5652436208', 'EUW1_5635258120', 'EUW1_5635253519', 'EUW1_5623616700', 'EUW1_5622146970', 'EUW1_5622091993', 'EUW1_5621222118', 'EUW1_5614492727', 'EUW1_5614473536', 'EUW1_5612018339', 'EUW1_5612000940', 'EUW1_5611821147', 'EUW1_5608618048', 'EUW1_5608670728', 'EUW1_5608555961', 'EUW1_5608515661', 'EUW1_5608304522', 'EUW1_5606931584', 'EUW1_5590031530', 'EUW1_5589975262', 'EUW1_5589489173', 'EUW1_5589511939', 'EUW1_5589417699', 'EUW1_5573887597', 'EUW1_5572127388', 'EUW1_5570898055', 'EUW1_5570865639', 'EUW1_5570864152', 'EUW1_5569482254', 'EUW1_5569390034', 'EUW1_5565660539', 'EUW1_5565464926', 'EUW1_5565500930', 'EUW1_5565378525', 'EUW1_5565355214', 'EUW1_5565094750', 'EUW1_5561682181', 'EUW1_5561474175', 'EUW1_5561128146', 'EUW1_5561058312', 'EUW1_5560950202', 'EUW1_5560931650', 'EUW1_5560915674', 'EUW1_5559487569', 'EUW1_5559482377', 'EUW1_5559365843', 'EUW1_5559232782', 'EUW1_5558946056', 'EUW1_5557745517', 'EUW1_5557638599', 'EUW1_5557538822', 'EUW1_5557480109', 'EUW1_5557432602', 'EUW1_5553594293', 'EUW1_5552981674', 'EUW1_5552935323', 'EUW1_5552106648', 'EUW1_5552046074', 'EUW1_5552030733', 'EUW1_5545605351', 'EUW1_5545499389', 'EUW1_5537302742', 'EUW1_5537274842', 'EUW1_5533851445', 'EUW1_5533714020', 'EUW1_5526429776', 'EUW1_5526359531', 'EUW1_5524591966', 'EUW1_5524516266', 'EUW1_5524410194', 'EUW1_5523619362', 'EUW1_5523585493', 'EUW1_5523600654', 'EUW1_5518139614', 'EUW1_5518144821', 'EUW1_5516559911', 'EUW1_5516574301', 'EUW1_5516561034', 'EUW1_5516497195', 'EUW1_5516462189', 'EUW1_5338711089', 'EUW1_5337141346', 'EUW1_5336878368', 'EUW1_5325952995', 'EUW1_5325860312']
    api_key = 'RGAPI-10ca454b-824a-4f06-9040-09015b569dcb'
    watcher = LolWatcher(api_key)
    my_region = 'euw1'
    name = 'LukyLucc'

    wrapper = Wrapper(api_key, my_region, name)
    matches = wrapper.getMatchHistory()
    x,y = wrapper.getAllDates(matches)
    toArray(x,y)

    print()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
