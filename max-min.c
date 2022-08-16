#finds maximum and minimum values of a list

int min(int* array, int arrayLength)
{
  int ph = array[0];
  for (int i = 0; i < arrayLength; i++) {
    if (array[i] < ph) {
      ph = array[i];
    }
  }
  return ph;
}

int max(int* array, int arrayLength)
{
  int ph = array[0];
  for (int i = 0; i < arrayLength; i++) {
    if (array[i] > ph) {
      ph = array[i];
    }
  }
  return ph;
}
