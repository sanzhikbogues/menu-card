// Authentication Token Interface
export interface IAuthToken {
    access: string;
  }
  
  // User Registration Interface
  export interface ISignUpToken {
    username: string;
    firstName: string;
    lastName: string;
    password: string;
    email: string;
  }
  
  // Recipe Categories Enum
  export enum RecipeCategory {
    Salad = 'SALAD',
    Burger = 'BURGER',
    Italian = 'ITALIAN',
    Soup = 'SOUP',
    Meat = 'MEAT',
  }
  
  // Category List Interface
  export interface ICategoryListItem {
    id: number;
    category: RecipeCategory;
  }
  
  // Predefined Categories List
  export const CategoriesList: ICategoryListItem[] = [
    { id: 1, category: RecipeCategory.Salad },
    { id: 2, category: RecipeCategory.Burger },
    { id: 3, category: RecipeCategory.Italian },
    { id: 4, category: RecipeCategory.Soup },
    { id: 5, category: RecipeCategory.Meat },
  ];
  
  // Category Interface
  export interface ICategory {
    id: number;
    categoryId: number;
    imageUrl: string;
    title: string;
    category: RecipeCategory;
  }
  
  // Recipe Interface
  export interface IRecipe {
    id: number;
    categoryId: number;
    name: string;
    imageUrl: string;
    description: string;
    steps: string;
  }
  
  // Master Class Interface
  export interface IMasterClass {
    id: number;
    name: string;
    date: string; // Consider using Date type if applicable
    duration: number; // Duration in minutes
    location: string;
    description: string;
    imageUrl: string;
    price: number;
    maxAttendees: number;
    attendees: string[]; // Array of attendee identifiers
  }
  