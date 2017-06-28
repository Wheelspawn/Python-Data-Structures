list0 = [10,0,1,7,3,2,4,8,5,6,9];
list1 = randperm(8);
list2 = randi(10,1,10);
list3 = randperm(12);
list4 = randi(14,1,14);

insertionSort(list0)
insertionSort(list1)
insertionSort(list2)
insertionSort(list3)
insertionSort(list4)

function insertionSort(x)
    for i=2:length(x)
        j=i;
        while (j >= 2) && (x(j) < x(j-1))
            val = x(j);
            x(j) = x(j-1);
            x(j-1) = val;
            j = j-1;
        end
    end
    disp(x)
end