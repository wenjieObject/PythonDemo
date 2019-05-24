using System;
using System.Data;
using System.Data.OracleClient;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            //var connectionString = "Data Source=(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP) (HOST = 100.100.100.221)(PORT = 1521)))(CONNECT_DATA = (SERVICE_NAME = prd))); User Id = pwoa; Password = pwoa";


           var connectionString = "Data Source=(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=10.60.4.205)(PORT=1521))(CONNECT_DATA=(SERVER = DEDICATED)(SERVICE_NAME=orcl)));User ID=R2E5FOUNDATION;Password=R2E5FOUNDATION;Pooling=true;Max Pool Size=500;Min Pool Size=0";

            OracleConnection connection = new OracleConnection(connectionString);
            connection.Open();

            Console.WriteLine("Hello World!");
        }
    }
}
