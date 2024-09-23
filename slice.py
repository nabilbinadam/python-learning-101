
fruits = ['mango','apple','carrot','pear','cherry','grapes']

fruit_dic= {
   
      'fruits':[['mango','apple','carrot','pear','cherry','grapes']],

      'market': [['tesco','alamanda','ioi']],

      'available': True ,

}


slicing=slice(1,4,2)

print(fruits[slicing])

print(fruit_dic['fruits'[slicing]])