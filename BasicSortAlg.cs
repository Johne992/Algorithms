using System

class BasicSort
{
	void BubbleSort(int[] arr)
	{
		for (int i = 0; i < arr.Length; i++)
		{
			for (int j = 0; j < arr.Length - 1; j++)
			{
				if (arr[j] > arr[j+1])
				{
					hold = arr[j];
					arr[j] = arr[j+1]
					arr[j+1] = hold
				}
			}
		}
	}
}


