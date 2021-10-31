#include <iostream>
#include <string>
#include <fstream>
#include <random>
#include <math.h>

using namespace std;

void data_generate(fstream *output, int num, double *mp, double *cp, double *mn, double *cn)
{
    std::random_device rd;
    std::default_random_engine generator(rd());
    std::normal_distribution<double> x1p(mp[0], cp[0]);
    std::normal_distribution<double> x1n(mn[0], cn[0]);
    std::normal_distribution<double> x2p(mp[1], cp[1]);
    std::normal_distribution<double> x2n(mn[1], cn[1]);
    for (int i = 0; i < num; i++)
    {
        double data[4] = {1, 0, 0, 0};
        if (rand() % 2 == 0)
        {
            data[1] = x1p(generator);
            data[2] = x2p(generator);
            data[3] = 1;
        }
        else
        {
            data[1] = x1n(generator);
            data[2] = x2n(generator);
            data[3] = -1;
        }
        (*output) << data[0] << " " << data[1] << " " << data[2] << " " << data[3] << endl;
    }
}

main()
{
    double mean_pos[2] = {2, 3};
    double cov_pos[2] = {sqrt(0.6), sqrt(0.6)};
    double mean_neg[2] = {0, 4};
    double cov_neg[2] = {sqrt(0.4), sqrt(0.4)};
    fstream *output = new fstream();
    (*output).open("./ML/ML_HW2data_IN.dat", ios::out | ios::trunc);
    data_generate(output, 200, mean_pos, cov_pos, mean_neg, cov_neg);
    (*output).close();
    (*output).open("./ML/ML_HW2data_OUT.dat", ios::out | ios::trunc);
    data_generate(output, 5000, mean_pos, cov_pos, mean_neg, cov_neg);
    (*output).close();
    system("pause");
    return 0;
}