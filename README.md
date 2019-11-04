# Start
//# define _CRT_SECURE_NO_WARNINGS
//
//1. 给定两个整形变量的值，将两个值的内容进行交换。
//
//#include<stdio.h>
//
//int main()
//{
//	int a = 12, b = 23;
//	int t;
//	t = a;
//	a = b;
//	b = t;
//	printf("%d %d\n", a, b);
//	return 0;
//}
//
//
//2. 不允许创建临时变量，交换两个数的内容（附加题）
//
//#include<stdio.h>
//
//int main()
//{
//	int a = 0;
//	int b = 0;
//	scanf("%d %d", &a, &b);
//	a = a^b;
//	b = a^b;
//	a = a^b;
//	printf("%d %d", a, b);
//
//	return 0;
//}
//
//
//3.求10 个整数中最大值。
//
//#include<stdio.h>
//
//int main()
//{
//	int arr[10] = { 15, 14, 16, 58, 14, 65, 25, 36, 2, 12 };
//	int max = arr[0];
//	for (int i = 1; i <= 10; i++)
//	{
//		if (max < arr[i])
//		{
//			max = arr[i];
//			
//		}
//	}
//	printf("%d ", max);
//	return 0;
//}
//4.将三个数按从大到小输出。
//
//#include<stdio.h>
//#include<stdlib.h>
//
//int main()
//{
//	int a, b, c;
//	scanf("%d %d %d", &a, &b, &c);
//	if (a > b)
//	{
//		if (b > c)
//			printf("%d %d %d", a, b, c);
//		else if (a > c)//b<c
//		{
//			printf("%d %d %d", a, c, b);
//		}
//		else//b<c && a<c
//		{
//			printf("%d %d %d", c, a, b);
//		}
//	}
//	else if (c < a)//a<b
//	{
//		printf("%d %d %d", b, a, c);
//	}
//
//	else if (b > c)//a<b&&a<c   
//	{
//		printf("%d % d%d", b, c, a);
//	}
//	else
//	{
//		printf("%d %d %d", c, b, a);
//	}
//
//	return 0;
//}
//
//
//5.求两个数的最大公约数
//（1）辗转相除法
//
//#include<stdio.h>
//
//int main()
//{
//	int a, b;
//	printf("请输入元素a，b： \n");
//	scanf("%d %d", &a, &b);
//
//	printf("a 和 b 的公约数是： ");
//
//	if (a >= b)
//	{
//		int c = a%b;
//		while (c != 0)
//		{
//			a = b;
//			b = c;
//			c = a%b;
//			
//		}
//		printf("%d\n", b);
//	}
//	else
//	{
//		int c = b%a;
//		while (c != 0)
//		{
//			b = a;
//			a = b;
//			c = b%a;
//		}
//		printf("%d\n", c);
//	}
//	
//	return 0;
//}
