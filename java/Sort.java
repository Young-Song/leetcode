public class Sort{
	public static void insertionSort(int[] nums){
		if(nums==null||nums.length<2)
			return;
		// the first element is sorted
		for(int i=1;i<nums.length;i++){
			int temp = nums[i];
			// find the first element that is equal or smaller than temp
			int j=i;
			// until the previous one element is bigger, right shift
			for(;j>0 && nums[j-1]>temp;j--){
				nums[j]=nums[j-1];
			} 
			nums[j]=temp;
			print(nums);
		}

		return;
	}

	public static void quickSort(int[] nums, int left, int right){
		int pivot_value = nums[(left+right)/2];
		int i= left;
		int j=right;
		while(i<=j){
			while(nums[i]<pivot_value){
				i++;
			}

			while(nums[j]>pivot_value){
				j--;
			}
			if(i<=j){
				int temp = nums[i];
				nums[i]=nums[j];
				nums[j]=temp;
				i++;
				j--;
			}
		}
		if(j>left){
			quickSort(nums,left,j);
		}
		if(i<right){
			quickSort(nums,i,right);
		}

		print(nums);
		return ;
	}

	public static void mergeSort(int[] nums, int[] tmp, int l, int r){
		//divide and conquer. sort two halfs and merge
		if(l>=r){
			return ;
		}
		int m = (l+r)/2;
		mergeSort(nums,tmp,l,m);
		mergeSort(nums,tmp,m+1,r);
		merge(nums,tmp,l,m+1,r);
		print(nums);
		return ;
	}

	// a subroutine of merge sort
	public static void merge(int[] nums, int[] tmp, int left, int right,int rightEnd){
		int i= left;
		int j = right;
		int k = left;
		//merge tmp into nums
		while(i<right && j<=rightEnd){
			if(nums[i]<nums[j]){
				tmp[k++]=nums[i++];
			}
			else{
				tmp[k++]=nums[j++];
			}
		}

		while(i<right){
			tmp[k++]=nums[i++];
		}
		while(j<=rightEnd){
			tmp[k++]=nums[j++];
		}

		for(i=left;i<=rightEnd;i++){
			nums[i]=tmp[i];
		}
	}

	public static void print(int[] nums){
		if(nums==null||nums.length==0){
			System.out.println("Empty array");
		}
		for(int i=0;i<nums.length;i++){
			System.out.print(nums[i]);
		}
		System.out.println();
	}

	//heap 
	public class Heap{
		int[] heap;
		int size;//actual element number
		int static cap=16;//total space

		public Heap(){
			heap=new int[cap];
		}

		public Heap(int[] arr){
			//index 0 is not used
			// actual size of elements is arr.length
			size = array.length;
			heap = new int[arr.length+1];
			System.arraycopy(arr,0,heap,1,size);	
			buildHeap();
		}

		
		public void buildHeap(){
			for(int i=size/2;i>=1;i--){
				heapifyDown(i);
			}	
		}

		public void insert(int k){
			if(size==heap.length)
				doubleSize();
			int pos = ++size;
			for(;pos>1 && heap[pos/2]>k;pos/=2){
				heap[pos] = heap[pos/2];
			}
			heap[pos]=k;
		}

		public int deleteMin(){
			int min = heap[1];
			heap[1]=heap[size--];
			heapifyDown(1);
			return min;
		}
		public void heapifyDown(int k){
			int temp =k;
			int child;
			for(;k*2<=size;k=child){
				child = 2*k;
				if(child+1<=size && heap[child+1]<heap[child]){
					child++;
				}
				if(temp>heap[child]){
					heap[k]=heap[child];
				}
				else{
					break;
				}
			}
			heap[k]=temp;
		}

		public void doubleSize(){
			int[] new_heap = new int[size*2];
			System.arraycopy(heap,1,new_heap,1,size);	
			heap = new_heap;
		}
	}

	public static void heapSort(int[] nums){
		Heap heap = new Heap(nums);
		 
		heap.sort();

		nums=heap.buf;
		print nums;
	}


	public static void main(String[] args){
		int[] nums= {3,7,4,9,5,2,6,1};	
		//insertionSort(nums);
		//quickSort(nums,0,nums.length-1);
		int[] tmp = nums.clone();
		mergeSort(nums,tmp,0,nums.length-1);
	}

}
