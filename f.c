#include<math.h>

double iterate_point(
    double X,
    double Y,
    double CX,
    double CY,
    int N
)
{
    double x = X;
    double y = Y;
    double new_x, new_y;

	for(int i = 0; i < N; ++i){
		new_x = x*x - y*y + CX;
		new_y = 2*x*y + CY;
        x = new_x;
        y = new_y;
	}

    double value = sqrt(x*x + y*y);
	return value;
}
