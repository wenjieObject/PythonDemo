using System;
using System.Collections.Generic;
using System.Text;

namespace ConsoleApp1
{
    [Serializable]
    public class DYQYDB
    {
        public string YDYMT { get; set; }
        public string WLZ { get; set; }
        public string RQ { get; set; }
        public string MATKL { get; set; }
        public decimal BY_SELLAIM { get; set; }
        public decimal BY_BVAAIM { get; set; }
        public decimal BY_SELLACT { get; set; }
        public decimal BY_BVAACT { get; set; }
        public decimal QN_SELLACT { get; set; }
        public decimal QN_BVAACT { get; set; }

    }
}
