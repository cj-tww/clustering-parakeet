# clustering-parakeet
Everything I learnt in completing the Applied AI course.

Folder Structure:
Each module is one folder.  

*python-recipes* contains random python stuff that I found on the internet or needed at work.


## Newest Hack
```
import qgrid
df = pd.DataFrame(index=range(0,<number_of_rows>), columns=['A', 'K' 'M', 'G'])
qgrid_widget = qgrid.show_grid(test, show_toolbar=True)
qgrid_widget
# <enter values into dummy df>
df = qgrid_widget.get_changed_df()
```

## Filter on ColA based on some conditions being satistfied in ColB

```
def select_group_if(x):
    value_counts_in_group = x[ <col_A> ].value_counts()
    if all(y in value_counts_in_group.index for y in [ <all_values_of_interest> ]):
        return ((value_counts_in_group[ <value_in_colB> ] == 1) & (value_counts_in_group[ <another_value_in_colB> ] > 1))
    else:
        return False
    
filtered_df = df.groupby('A').filter(select_group_if)
filtered_df

```