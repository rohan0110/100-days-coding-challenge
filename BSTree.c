#include<stdio.h>
#include<stdlib.h>
struct bt
{
int info;
struct bt *left,*right;
}node;

struct bt *root=NULL;

struct bt* getnode (void)
{
return  (( struct bt* ) malloc (sizeof(struct bt)));
}

void freenode(struct bt *p)
{
free(p);
}

struct bt* insert(struct bt *r,int x)
{
struct bt *newnode;


   if(x==r->info)
	printf("\n Duplicate Values.");
   else if(x<r->info)
    {
       if(r->left==NULL)
		{
		  newnode=getnode();
		  newnode->info=x;
	  	  newnode->left=NULL;
	      newnode->right= NULL;

		  r->left=newnode;
		}
	   else
	    insert(r->left,x);
    }
   else if(x>r->info)
    {
	if(r->right==NULL)
		{
		  newnode=getnode();
		  newnode->info=x;
	      newnode->left=NULL;
	      newnode->right= NULL;

		  r->right=newnode;
		}
	else
	     insert(r->right,x);
    }
}


void search(struct bt *r,int x)
{
 int found=0;
 struct bt *temp;
 temp=root;
    while(temp!=NULL)
    {
      if(temp->info==x)
	 {
	   printf("\n The %d Element is Present",temp->info);
	   found=1;
	   break;
	 }
      if(temp->info>x)
	 temp=temp->left;
      else
	 temp=temp->right;
    }

if(found==0)
     printf("\nElement not found");
}


void inorder(struct bt *r)
{
 if(r!=NULL)
  {
    inorder(r->left);
    printf("\n\t %d ",r->info);
    inorder(r->right);
  }
}

void preorder(struct bt *r)
{
 if(r!=NULL)
  {

    printf("\n\t %d ",r->info);
    preorder(r->left);
    preorder(r->right);
  }
}

void postorder(struct bt *r)
{
 if(r!=NULL)
  {
    postorder(r->left);
    postorder(r->right);
    printf("\n\t %d ",r->info);
  }
}


void main ()
{
int ch,x;
struct bt *newnode;

while(1)
{

printf("\n  ----- Linked List -----");
printf("\n 1. Insert");
printf("\n 2. PreOrder");
printf("\n 3. InOrder");
printf("\n 4. PostOrder");
printf("\n 5. Search");
printf("\n 6. Exit");

printf("\n Enter your Choice : ");
scanf("%d",&ch);
switch(ch)
	{
	 case 1: printf(" Enter the node value:");
		 scanf("\n %d",&x);
		// count++;

		 if(root==NULL)
		 {
		  newnode=getnode();
		  newnode->info=x;
		  newnode->left=NULL;
		  newnode->right=NULL;
		  root=newnode;
		 }
		 else
		   insert(root,x);

		 break;

	case 2 : preorder(root); break;
	case 3 : inorder(root); break;
	case 4 : postorder(root); break;
	case 5 : printf(" Enter the node value:");
		 scanf("\n %d",&x);
		 search(root,x);
		 break;
	case 6 : exit(1);
	default : printf ("\n Wrong Choice");
	}
  
}  // end of while


}