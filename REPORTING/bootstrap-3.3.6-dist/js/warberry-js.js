
$('#warBerry_tabs a').click(function (e) {
    e.preventDefault();
    $(this).tab('show');
});

$('#responder_tabs a').click(function (e) {
    e.preventDefault();
    $(this).tab('show');
});

var pdf_contents=[]
localStorage.setItem("pdf",JSON.stringify(pdf_contents));
var pdf = new jsPDF('p','pt');
makeReportingPage();
findResults();
createDropDown();
createPDFile();

function makeReportingPage(){
    var imgData='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAUAAAAA5CAYAAABHyvIXAAABH2lDQ1BpY2MAAHjalY8/S8NQFEfPCxZBMEYI4vhAEIVqjYrYse1QBMEaOiTdmjS00tg+0lf/fAcd3Tp08Rs4Ozu4CU4OfgRBcOrgkEpwKj3L/d3D5V4uGLKpVGxYcNnTiVstS89vyMVPctgsk6PQDAeqVKudAvzV//y8IwDedppKxczHUisahMAE6IYq0SA6wMa1VhrEHWAHXaVBjAE78fwGiCfAbqf5BbCDNH8AdlJ3KyC+ADOouxUwAMx2mi3AnN4FWC21+kEk3WpZbjnF4vH2nD/MREc3GqDSV7fJRbujZUmpOJInvXA3L/f3nCPw/IZMp7/PEYBYe81cRuZG63D2CAuTzB3ewzgPKw+Z23TAKsDzKBwmV9M1wjiAWf0vEj9KUZtdyr8AAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAAXEgAAFxIBZ5/SUgAAOltJREFUeNrtXXdYFce7fpfOoXelI0pREVEUCyiIoIIdayxRo8Ze4i+WxMQSe4816s9ubIgFxa4UsaMoqIhK772DgDD3Dzgnp+zZM8eS5N7L+zw8D2d3Z3Z2Zvebma+8H9CEJjShCf9PwYgfSEtNJQmJiWjRogUsLS0ZrsLl5eUEADQ1NSWuq6ioIBoaGqzly8rKyOPHj6Gnq4vmpqbIz89HXm4u9PT1YWBgAD09PWhpaXHeGwAyMzNJYUGBxHE9fX18/PgR+vr6VPX8m5GdnU2aNWv2jzzDkydPSGJCAiwtLcEoKKC6uhofPnxAdXW16N+HDzAyNsbw4cMZADh37hy5du0aGIaBiooKSkpKUFpSgpKSEtTU1gIAVJSV4dqpEzZu3Pi/enya8L8bDACkp6eTPXv2IDYmBjExMYKTKqqqsLayQnJKChzs7fHhwweUlpaitLQUlZWVguuGDBmCrdu2MQAQeOYMWb58OSoqKgAAqqqqsLe3x/oNG+Do6MgAwJQpU8jNGzcE5bW0tDBmzBjs27cP9fX1DfdWUYGenh70DQxQXV0Nt86dsXbdOsHHsnLlSnLwwAHWh1JUVERdXR0AwNHREcNHjMCkSZPk/tByc3JIQmIiVFVVoaysjPLy8oYThCArOxupqamwtrICT0MDaWlpMG3eHP38/JgnT56QqKgotGjRAgUFBdDT1UWHjh1hYmLCpKenE3Nzc6q2XL58mcyeNQtqamrQ1NQEwzBQVFSEsrIy1NXVoaOjA0NDQ1haWaFjx47w8fFhgIaJadPGjVDn8WBlZYX8vDwoKikhJTkZ9fX10NTSgqOjI/r06QNtbW2pbenXty+Ji4uj6ittbW3ExMYyAODq6kry8/Koym3dtg1DhgwRtCE9PZ2kpaVBS1MTNTU1qK6paejy+npkZGQgIzMTLVu2hKKCAtLT02Hv4IAePXowYWFh5G18PGxbtkRGejpMzczg4uICHo+H4uJiNG/enHr8i4uLSVxcHBQVFaGtrY2ioiLBuby8PCQlJcHU1BT6+vpIT08HT10dw0eMYOLi4kjonTuwsrZGZWUlVFVU4NKhAywsLJi01FRiIWNBIY64uDhioK8PYxOTf90kkZSURPbs3g0AMDA0REF+PgDgQ3U1MtLTkZubC2NjY5iZmyMvNxclpaU4duwYDAwMGAA4dvQoOXnqFMpKS6GgoIA2bdogNzcXW7dtg4WFhcznHRYQQF6+fAkjIyMYGxvDyMgIRkZG0NDUBACkp6cL/vLz8mBsbIwOHTpgwsSJ6NKli6B+JQB48eIF/jx+XOImNdXVePv2LQCICEZxhIeHAwBSU1NJLy8vfPz4UXCuuroaMTExeP/+veBY5N27IuUtLC1hY2MjEH4AUFNTg5ycHOTk5AAAenh4iJQ58eefrG3p2LEjNDQ1EdHYpri4OKxcsQJTJk8m+//7X+oXqaqqigwaOFDw/DSwt7cHANy+fRt/7Nkjcd6uVSvi3r07uri5EU9PTwwaNAhdu3WT2qbfVq4EIQRVVVWoqqqSef+FP/5INmzcyDx5/BiHDx+Wef3aNWtw7epV0rdfP4k2REREkPHjxlE/e2lpKV69fEnMzM3R3tmZulxWZqbg/8LCQuLv54esrCzq8j169AAABF+8iHPnzkmcV1FRQU1NDTzc3UmvXr0wZOhQtG/fnvM9mDZtGh4+eEDdBh0dHQDA48ePsWHDBonzdq1aEQ8PD3RwcSE9e/ZE/wED4O3tLdKGvXv3EiUlJVw4fx62trYYOWoUvp86lT/JEqBhkiktLUWnTp0QePasXEKxrKyMxMfHw9XV9YsI05kzZ+L1q1ec16SlpeHp06cAAAUFBaipqQEAVq9aRfbt24e0tDTBtSkpKQCAdWvXAgDi4+PJ7FmzsP+//4WVlZVIm48fO0aWLl0quIdwPdKQm5uLa9euwcLCQuS4AgBoaGh8VmfUNm5rzp07JyL8+DAzN8eAAQMED8H/mCdMmAAzMzPEvX6Nn3/+mfMejo6OIr8/fPjAet3Lly/h6uoKHo8ncvzmzZsIvniR0D7T3r175RJ+ANChQwcAQFFhIev5msbVTHZ2Nk6dOoXRo0dj8ODBJC0tTaJdVVVVpLq6Wq77c01SbCgsLMT06dNx4fx5ifsfoRCg4nj48CFevXoFZWVlucsCwKaNG+USfgDg4uLS8CxCqzRh8Ps8LS0NR44cweBBgzB+3DhSUFDA+i6cPnWKyCP8AMClcdwLZYx7YWEhzp8/j+8mTYJP797k9evXBGgQTtu2bsVvK1ciNjYWFy5cwOhRo5CamipST2lpKQDgyZMnCA4Opn6Xq6qqSH1dHUpLSkSOR0ZGkkEDB5Lk5GTqugDgzOnTRJbwE4e9gwM0NDSYx48fk/3790sVWiEhIejWtSsZNXIk3r59y7owe/funVz35oICAFhaWn5yBaqqqhg3fjwA4Mnjx6zX5OflITAwUNDJ3bt3R/fu3TFv/nz8sGABWrZsiatXrwIA+vTtK1He0MgI/fz8RI5NnToV6urqEtdWV1djy+bNIlt0Pq5fv079XOIrzDZt2sDd3Z2zTIsWLQBI/xjZ8Dw6GvzZTBjq6urMzl27oKCgQF1XZuNqSktbm7oMIQSLFi3C+3fvRD4CP39/zJw1C4aGhtR1FRUVoXv37sz9Bw+wfv16DB8xAv3798fhw4dhZ2fHWfZDVRU5GxQkcszDwwNt2rSh6vNiOfo8IiIC69etYz134sQJkd9m5uboP2DAF2/Du3fvMH/ePABAWFgY1QpfGGvXrEFlZSWn4Pr999/JggULSBc3N6xduxYvXrzAtO+/J0sWLyb+fn5kwrff4sWLF4h/80aue9+6fVuu6wFAsfE9zs/PlzlBZmZmCtQOBw4cwKKFC0Wes7Obm9z358NcbAWoBAAtWrRgNm3cSPLz85GQkIAnT55IFGQYBjweT6DbA4ClS5diaEAA9PX1GQAoKi7GnDlzsH37dpGy1dXVWLliBcrLy4mmpibz54kTDAD82fiyTfv+ezJ58mQAQGJCApydnQUrPl1dXYz+5hsJXdVPP//MVFZWEn8/PyQlJVE9fGRkJP2AKSqK/E5OToasaZK/zTczNcWgQYPw9t07xL1+LfNe4WFhiIyMJO7u7iLP6O7uzuzbu5esWbOGqs3W1taIiY2Fq6srk56eTqKjo5GclISgoCAkJydLLVddXY0VK1aIHAsICGAAwKd3b5LfqN+RhlatWiE1NRWGRkYAACMjI5Hn2LlrF27evEmmNI4xGyqrqqDB46FGaNUbFxcHbRnCPDExUfDsVlZWePnqFRKE1C3ScO7cOcTFxRG+XloacnNykJ6ezllXQkICgAZd2MBBg5CakoKYmBgRlQ4b4uPjERgYSJycnNC9e3c8ePBAZhk+srKysHvXLqnnCwoKSNeuXVFTXQ1FRUWcOnVK5DyPx8PuPXtgb28vscWUhf79+yM1JQVv5BCcfIHm5+fHlJeXk6LCQoRcuYIrISHIysrCDwsWYOuWLcjNzRUpV1dXJ5jY+fD392eKi4vJuXPnsFLsveWCj48PRowYgW+//VZwTOLBIyMjydgxYyQK+/bpg8SEBBFd3vMXL6Crqyuow6d3b2Jmbo6y0lLB3l8Y27dvx8BBgyTu2a9vX1JaWoqMjAwAwODBg7Ht99+pBuXQoUNkxfLl1J1w7vx5dOjQgaruyMhIEhkZiaNHjrCuKMUxcdIkLFu2TKTu5ORksnr1aggbfdjQsmVL3Lp9m7Vdvb29yXuKj9rM3Bz37t2TqCMzM5P07NFDoKqQp2+6dulCZG1LzwYFYfOmTRg7bhz8/f2l9u2K5cvJoUOHRI4tXLgQM2bOZICGVeC9+/dx//59HDp4kEoYLF6yBNOmTRO5Z1xcHFm+fDkePXzIWbZr1644eeqURHufPHlCIu/exfHjx1HA4mUgDj8/P+zes0eknuzsbLJl82acOXOGs6yBgQHuRkaCx+MxpaWl5PXr18jNzcXSn38WbHmlQUVFBTdu3oS1tTVrn6ekpBBFRUUsX7YMt27dEjm3afNmDBs27LP0gTk5OWTxokUIDQ2VeS3X+83Htm3byLatWyWODx06FFu2bpUo+/btW+Lr4yPz3v0HDMCaNWtYDX4S+ytpW44b169LLF2FVwbXr10j7969g6KCAp4/f85ax10pK7Be3t64dv06VFVVATTokmgxceJExrdPH2q9U0REBHXd7u7uzOLFixnaWVlDTO8IANbW1sz+/fuZ9o26Kml4//49bt68ybrIVFJSorq/uIKXD1NTU8aZwjDBpvcrKyvjLBMQEIAb16+jvr5e5nZ5zty5EvpmntBvNXV1xtvbm5k9ezb1Soitzx0dHZnTp08zslQ7Dx48QExMjESfd+rUiZn/ww+MZqNFURbUWdrQrFkzZsPGjQybSkcYBQUFCDp7FgCgra3NdOnShRk4cCAzd+5cmfetqanBco7J38rKijE3N2fsHRwEx86dP4/DR458tvADABMTE4ZWTy3LzlBaWkrEDZ18BAcH42lUFJG3Tj5aOzpK9XaQEIB6enqMmZmZxIUMw4CQv9rg4OAgsNwAQESjZff27duoq6sDj8eT+CCePXsmUW92djaZN28e7t+/L9Dp8eQ0yuzbt4+ZMnUq6zllZWVcuXoVnTp1amhno3WYFrk5OUSawUUcXO2msYxK01HyleiywLVdbG5qKrP8jRs3JPRKwioPNgQFBWHfvn149OiRTAGop6fH9PL2Fjlmz6IbpLHq8cHV57L0hwC3Xpi2HWxCmA8XGROftDZ8N3kyY2NjI7NsWGgorl65wjpxpqSkkJCQEBIVFSU4FnzxIjw9Pb+YW02xmGFFGngcfXTr1i3S3tkZI0aMYD3/8eNHBAQE4NXLlyLPaWZmRvUcFhwTIauGvTXLi0MIEdnzKyoqiui3ngp1MtBgGRbXHaWlpuJDVZXIQxw+fBg7tm+Hk5MTPD09AQA9G10b5MHChQtZO+PAwYNwdHTEzJkzAQDPnz9HSXExtdVLtdF0TwOuGYlmC5vUqM8SRzWlAOSCkphOkw1VVVV4JWTdKysrI8KTnizQGExcXV0BAFZWVjAzM4OyiorENery9DnHh/U5fQ5A4LYhC7zPHXcp+tmfZHhG8LFixQqUlZVJDNTeP/7AzBkzRFQBbp9hQGCDlpYW1XVc30bzZs1QX1/P6kHCh4KCAusEz2YIFYe0nREgRQC2bdtWZqWvXr1CTGwsgAYzu7jLCJu+ycLSUmJWjYuLw/bt29Gta1dcuHABAODp5UXVqTT4ZelS7Nq5E5cuXQIA1NfXI/LePeryOjo61LMl1yxn1+gjyAVpOroaym1GGYfOqJbj5RJ5BqEXSuD4/QX7ysXFBXPnzUN4RARz7/59hs0vTR4rNpfwsf+MPgfk+Lg5xt1ehvUbkD6+Pj4+TPfu3WWWz87OxkYx/8Pz588TcYv24MGD0c/P74s6VWtT9hHXOGk3+lEKw9zcHOvWr4eKigqGDR+OS5cvQ15Hcj709PSknvtkAQj8tep78+YNlc4m4f173BRSxmZlZZH8vDyMb3SjAQBNTU307NlT7gcNCQkRmQH7DxiA5s2bIyUlBZs2bUKQkIuFvNtgWl0Q1yxXLkOXxgXaLTCXfxSNMGMYBlbW1p/c5uzsbJnLxXbt2jHz58/nHF9awQNwTzrlMrbvsiDLAi1oA9e4U7SBYaR3x9JffqFyhTp69CgePXok6P9LwcEAGnS0Hh4eaNasmYSl/0vgS0wSbC5Ai5cswciRI+Hg4ID58+ejTZs2nyy4hVV14vgsAVhQUIB3b9+SNDGHTS6ECVmMYl68gJ2dHeqEhKcPhVWHj8DAQOLr40OeP39OvL29BSsHHo+Hj7W16NChg0D3J4y7YpEoskA7yDyO5XguRWgY3wgkDloByLXiyZDhygEAzu3bi8R1l8m5AhR3V/hU8Hg8RpFiy954rdRz/CgiLkjrc0COcedoQy5FG1RY1AB8ODo6MqNGjaJqx38WLBBshQcMHAigYVLMyMzE+g0boCPksfGlQNtH6hx9xOZlEHT2LGprazFk6FC8jY//rDZaC03q4mAVgCYmJoxRo0+XLNy7fx+mLEYTNowYMQIJCQkoLS0lALB//36cP38efx4/jm7dusGxdWuMGj2a+sH++OMPvH37FksWL4aqqir6+/tDSUkJs2bPhmPr1sjNzYVXr14S5TIzM/H+/Xtq5ZYC7cfIsRKg+RilvUy0AlBDykq1pLiY8H3VuDB8+HCR37IswOLIzs6W63ouKFJavrlW3XliPmVs4PqAaZ3QuVY3uTRtkLHSnP/DD1S7kLS0NEFE1ZAhQ5g1a9ciPT0dXbt2/aRdFQ1KKI0gXH3EFm8eGhoKL09PXL50CVeuXkVeXp5c0SrC0NXVlXpO6gg7OTlRVR4RHg5nZ2e0sLXlvK558+bIzctDcXExIiMjUVhYSIStwvfv38esWbPg5uZGNVCFhYWE7/AaFxeHyMhIDA0IwK5duzB9+nTMnj0b1dXV2LB+vUTZPn37omXLllT3qaioIDSrJ4B7kNMpLIrm5uasx/nEDp+KwMBAmSoKKysrjBkzRqRP5NUByhvGJg3JycmEVu8pbfVVUlxMaHz4pPU5QB9yxTXxJXE4oNO0AWhwLJ85axZVW4IvXsSZ06cJAHzzzTfMs+hoZvXq1V+NTIFWAHL1kTQf2YyMDDx9+hSBZ85g27ZtX6X9ny0AHzx4gLq6Oiz88UfO67KyshAWGoq6ujqEhYaipqZGwoIjy1lYGDExMSK6k8DAQLi6uiI8PBxv3rxBcXGxVB2OibEx9X00NDSYz9UFBZ45Q2hWU2yqB1nhTtKQlJREMjMzSVBQENm0aRPntYqKiti0ebPEcR0W5TQXIiIicPLkScL/27F9O5k3dy7ZuHEjOXHiBDl58iQpKiqS+TyGhoacejFhSFsBHjt2DDQW7DYc6h4TExO6NkgRwnfv3iWJFCtvGpXT9OnTGS5rpjCWLVuGhISET14xyYOPlMY1aX0UEhJC2IImhKGsrIxxchBzyAOp+wyndu2oKqiqqsLDhw/RtVs3KCgooL6+Hvb29igqKpK6/K+trYWJiQlGjBgBfmSAu7s7vhkzBtt+/53qvocOHRJ5wW/dvInqDx9gbGKCfjKcT0+ePCmVBUUcZWVlxIlSJ8o2yOfPnyeLFi3iLGdgYIDCwkJ0Z4k1rqmpwbDhw+Hj44Ply5ZRr7I0NTXR399fYuvdr18/jBgxArUfP2LqlCkAgLVr16JTp04SfaErpwAMDwtDeFgY5zU0W/GcnBwq4dUYninR7oMHD5JVv/0ms88rKipYdcR80PY128QXeucOmdXoesXVhoKCAgGjjSws+eknzJg+XeZ1VVVVmD17NlWdn4tPdRVKTU0lJ06cwNw5c2SWbWVnBwcHB9ZvVUVFRe44amFIXQG2k7ICZFsV3Lp1C9ra2mjfvj0AYN369ejYsaPUmyanpCA9PR3evXsLjkVGRuLC+fNUjS4uLib3xKJKKisrcf/+fQwdOlRm+draWkybNg1z58yR+ZVpaWkxVlZWVO3ikyDcunWLbN60ifT29ibz582T6cZiamqKHj17sjp26urqMj///DPc3d3x54kTGEs5E6qqqrKGcenp6cHTy0vgGrBi5UqMGDmS9eWqpHyxvLy8MGbsWM5reDwezM3NZW73AMDW1pah8e9SUFBAbm4uAYBrV6+StWvWEA93d7JyxQqZW35TU1MMHDgQ0kh7AXZ/WDbwSXnv3btHdu7YQQYOGEAmTpwoc3toamoKBwcHuLi4UC13/fz8mM6dO1O1iXZr+rmgcdYG/vKHPH78OBk9ahSZN3cunjx+TLWC5OKWPHzkCKeODwDnZCpVABqbmDDNmjWTOL5ixQqIR4rcvnULhBD0bHRkDr1zh9OFIPrZM2zbuhVubm4iArV169ZUnXn92jWJjlNWVoaamhosLCxA+5JcunQJ0miRhMFlpRMGX2e2Yf167Nixg8oJFmjQYS5cuFDq+Z+WLMGUyZPx+vVrRLNE07Dh8OHDrC/XiRMnMHjQIPzSyEBz5PBh3L93j7UPaFiCPL28cPDQISxcuJDToHDy1CncuHkTgwcPpmo/TWhjXV0dqhujdJYsWYK9e/dSR28kJiZi3vz5nNeo0o57o6vL3r17sWnTJmpastjYWCz56Seqa/n45ddfqdQDtEbMLw0LCwu0Y9k9mjVGItXV1eHBgwd49uwZZG19VVVV4eXlhaPHjkm9xsXFhTl48CBnPUUcLD2cZq52LOFb8+bNE5AW8JGVlYUXL14IIjmCgoJw+vRpzkbduHEDDMPAT4jmqrsMuik+hIkvVVRV4dalC06fOYOu3boBAIYGBIhc38LWFitXrpRYfdTX1+POJ1D7sEFbW1tANimv9XTV6tWcfk57/viD6du3L2bNnCkSqcGF59HRUs+9ePFCENWTmJiIMWPG4MiRIxJCkIbVubSkBLW1tdDW1gZX3OvMGTOw8McfOV9GeWFtbS1wjpUVsicMZWVlbPv9d5iamn62cUBRURFdu3YFIP+4z//hB7mts05OTowsgyMAwcTwd0NZRYXVes5f6NAw9fDRpk0bHDp8mJG2/eWjha0tTE1NpeqDuTwwOH0N2js74wYlh971a9ewcNEiGBgYSAhINpSVlSEpMRHDhw/HyZMnYWZuDhsbG5kvQ1pqKvFoDJpmGAZPHj+W8CT38/PDsl9/BT9QOzEhAZH37rHSGt2Qw/DChYkTJ2L+Dz8AAPVHbmJiglWrVwuo7KVh9uzZZOXKlXK1Z8rUqbCzt0fonTuIl+FHRQjB8mXL8DQqinQUisygGcdnz57BrXNn2NjYoF27dgKKM6BBLfHu3TtUf/iAZs2bw9PTUy5qeppnDAsPR25uLulCGeJlbW2N9Rs2UHsbyEJAQAAMDQ0ZgG7CABqEwdKlSzF8xIhPagON7528ZLpfCrKMPjS2BQMDA3w3eTJmzJhB1T+6urpMWFgYcXNzQ+CZM1i1ejVqqquhoKAAe3t7znA5TgHo3KjTo8HVq1exaPFieHp6ikRdcOHtu3fw8/NDhw4d0LJlS9yjCFE7KcRrNmTIENy8dQsBYis+LS0t+Pj64nJj+BsAqYI8PDwcpaWlhCs3hhLHdszAwACbN2+Gp5eXoPzQgACplP1Ag9vDmLFjMX78eE4dFACUlJSQvn36SNWVqKiqomePHhJEE127dhXUGxkZSRYtWsTpDE0IkRg32jjgoqIiFBUVoUfPnujevfsXESxcagcLCwts3rIFnTt3ZgDA2NiYmfzdd0Sc8kkYti1b4tvx4zH+228Z2nhYrm24mpoaNm3ejP79+wued8SIEdjMYk3nw9DICKNGjsTkKVNEaOTkhZ4MnRcgnTH9n8bw4cOZeXPnkuDgYLRo0QJOTk6oqalBXV1dg/rKzQ0e7u5QU1en6p8tmzeTHxYsYIQJHp49fUpMmjWDmZkZk5iUhKvXrkktzykA27VrJ8ECIw0pKSl4+fIlvHv3phaAhw4ehJ+fH1avWUO9tTstJADPnTuHV69eiazi1NTU0K9vXwwLCBARgNJQU1MDrg8HABzs7VmJTdu1a4elv/wCUzGmlV69erEKwP79+8PFxQWt7OygqKiIPIoVQ11dHfLz86GkpCQhBD29vLBjxw6oq6tz6k/d3d2ZjIwM0rdPH4ltmqKiIvr37w8lZWVBxjY+uBx02dpDqyulgZ2dHdiIWHt6emLa99/DVmwb2MvbW2IcGYZBwLBhcG7XDlbW1lBVVUVqaiqRle1Q0AZ7e9xmUZFYWlpi85YtElbyXr16sQpALy8vdOrcGa1bt4aCggJkEczKgq6ursDjon///ggLC5Pw2fy3CkAAAq7PxKSkT2KXFsYPCxYwALBu7VqiraODFjY2GDdunICdShY4BaCWlhbj07s3oXUIvXzpEmbPmSNIRCMLUVFRuHfvHsSZkKXh9KlTZNGiRdDS0oKBgQGSk5MRHx+P1q1bIzg4WOAwHHzxIq7fuAEjIyMqISPL+izOkM1XQm/ZsgUtW7WSaHv37t2hrq4uYZ6/fPkyLl++LPitqqqKkpISIotEQFrAfklJCSoqKqCpqQktGZECZmZmzOJFi4g4M/CwYcOwrtFZ/MqVKxD2GZS21Ro7bhzmz5+PkSNGIDMzE9999x127twpt98gF8QNCQzDQE1NDRs3boSxsbFEf3mL0WwBDSvYs4GBOBsYKDhmKIdxIIpl3AkhWLduHavbUJu2bZluXbsS8ZDA0NBQCdLQ5ORkIo3IVBa0tLRgYWGBVq1aobS0FOXl5bCysoKxsTEsLS0RFBT0rxaAXxI3btwgPy1Z0pBeNy8PmzZtgomJCb4dPx7v370jbN+nMGTG+vAT/dDgckgIVFVVwcZgIc3ixsYAKw0HDhyAtbU1wiMiEBoWhh07dwIAzp8/LxEtERsbi0EcFkcejyeIIrh7967UQP7y8nIiLMjatGmDoQEBaO/iAmmdq66uzvTo2VPm81RXV+NiIwMOFzQ0NFgtf9HPnqGHhwdGjRol0+0hKSmJsEUl1NXXCwwI4qzX0gRg8MWLyMjIwI8LF0JZWRmR9+6BEEItANNSUzm3FOnp6UT4ebt16wZvb2/07NmTVfgBDeGbLhTvan5eHq5fu0a1txdeqVlYWGDCxIkwNTVFN45tfp8+faj6QJaRkAupaWkYO3YsIiMjBQS/o0aPhrq6ukCN9G8RgOrq6nBwcKAmlpAXOdnZyM/Px6aNG3Hw4EHo6+vD2dkZL1++RO/evdGrVy/Osf6iAjAjPR2PHz9Gv379JM5JE3RRUVGIjIykeiETEhJgbm4uSLCiq6vLGujs4OAAn969JXSDwuefv3iBB43ZvwghEjkT+NDU1GT4pJY2NjYCk/zaxvR90uDv70/VZ6coPgQNDQ20bNmS9VxNTQ0ePXwo059q9apVrBTxZwMD0bFDB0ybNg2GBgYi56QJwNLSUqxbuxZbNm9GSUmJwDWHNjB+x44dnOfNzc0Z/rg6OzvjvwcOQElJSWbmQH+xxFlS+1zKWIuD75VgaGiIP0+cAMMw2CJjwvajHHfhVam8yMnJwZYtW0RUU1u3bMGzZ88E8di0jNqfC3GaNUNDQwi7z307YQLGf/stdDkoqT4H/Hw5ZWVlqKiowOPHj0XUFq0dHUVYcsQhUwB2bCSwpAUhBH3koKgHGrZeshB65w6pq6tDZGQk3N3dsX79enw3aZIg2Y+9vT1cOnSAtrY2zM3NoaOryzg6OjKOLLqxN2/eICgoSCQqgS39Hh/zf/gBlpaW2LBxIx4/eoSI8HCMHTsWV69cIbt37ybbtm0jEyZMEOnk3r17U1F2v371CrGxsVIHSFlZGcXFxVRxqbUcaocMFqaWKVOmwKVDB1RXV+P6tWu4c+eOyHm+dZMN9+/fl7Au05AHrFq1ilRWVSHwzBmSnZ1Nrl29yvrsPy9dCjNzc/DzqURERGDSpEm4dOkS+eOPP8ia1avJzBkzJCjQaNoQHh6OrKwsmZPu1KlT4ejoiDVr1yI+Ph5hYWEYP348QkJCyL69e8munTvJuLFjCd8ZG2ig0zejcPbOy8vDjRs3PilcraamBoaGhujS6H7DPyauBywvL//q4XAlxcWC/5WUlLBs+XI8ePhQ4N6WmpICB3t7Qea8r4n27dtj0KBBCBg2DDt27oRbly64fPkysjkiemRSbrRs2ZLp4OJCpOU8FYa2tjYcHBygo6vLTJ06ldC60OhRzA7CwdBlZWWCxOPr16+Ha6dOsLW1FXysfKJWAAgYOhSrWAwYSxYvFvmdl5eHY0ePknHjx0t89EaGhjh48CAePnwoksJyulhYUllZGdHS0mKABkonNp0bG7iu0dLSYkaPGkUeCOWqbdGihSAbmjCyOfydUoS2vwYGBujRowcWLFiAVatX43l0NEzNzDB7zhz8tmqVSDkVVVVqQlZZSEtLI16envj48SMuX7qEGTNnSl2ptLCxwcGDB3HlyhX83jj27969w2whUgBxIoRmzZoxEydMILKS9NTX1yOQYgWmpqqKnbt2ISEhAcIZ7WbOmCFynbAQABpYdWhUO6cpV6LiUFJURAJlQvCvDWGXL0srK3g1khnzHbGvXLmCK1euCPTMXxM1tbXQ0taGo4MDDA0MMHv2bCxfvpyTqZyK76cTZWTF1KlTBauGUSNHUje8efPmnOd//eUX8uLFC4njDg4OGDlqFCMs/MQxcNAg0HLL/f777ygsLBSZNSsrK8ngwYPh5+fHmr9XGFViOrRvJ0ygum/wxYucpAd79+0T9JGbmxuuXrvGGuspzc0lKSmJ8PV7WlpaOH/hArZu28aoqasz7969g5KSEvbt3cuqX6Nl/DUxMZGZg+Pjx48YOWqUIMnT4UOHBGFkwkhJSSFDhg5F3z59BMKPDWy+bhMnTaJqL40ObvQ332DggAGCmGlpqBAb929Gj4YKB88gH6GhoVQksuIQ98qQFQr2NSGcEyQxIQGzZ81CXV2dBM+iPA7Q8kB4Enz96hWOHzuGJUuWYPTo0bh//z4cHR0Z8TStwqASgLR+UwHDhgn+7+XtzbRq1YqqnDSWiw9VVWTBggXk6NGjrOdHf/ONzLqNjY2ZdhQJiYAGpff0adOQnJwseMMy0tORmZlJZdUWz3rn6OjIDBkyRGa5srIyLPjhB5w9e5b1Y9DW1mb279+PdevX4/CRI7h29Sp8+/TBd5Mni2SMa7QIStTx5PFjtLC1haamJtzc3CDsBtKzZ0+sWLkS0rZttHq96TNmCPJDi6OkpIS8efOGWFtbY9WqVYKVc2VlJavuMi0tDRnp6TLdrxpVIiIX9ejRg4pGPiM9Hf/5z3/IFSkJhUpLS0nC+/dUESbicenGJibMd999J7NcfX09Fv74I44fP07Ec+VIQ05ODhHP8VxWVsYak/vo0SNB/9PULS9evHghwXYTGhqKXl5e2Ldvn8jxixcvfrF2JCQkkKlTp5KJEyYQtqCDZs2awdDISILfkg1UZvg3b96QvmLWrXnz54ss8+3s7HDj5k2R+iIiIsh4iuD9Bw8fikQIREREkCePH+PK1aucM4eHhwemT5/OaZXbvn072cLhnCoNrp06wcnJCeeCgug5z3g8zJk7FwEBAYLk4NnZ2aRrly7UTsX+/v7YtXs357gsWbyYXL9+HeUVFejatSteN/pQ5uXl4cbNm7Czs2OABk48HV1dZvy4ccTNzQ0VlZU4duwYfH19MWbMGKr8yN7e3oRm9u7p6YnNmzeL6A1LSkrIoUOHcODAAaiqqCAyMhKqamq4cf06vv/+ewANesifly5lACA2NpacawyjpMnDDDSoT+bPn49BgwcLcpK8jI0l/fv3px5r4XzOaamp5MKFCzh27BgVmSnQoPuaPn06RowcCQsLCwZo2Dm4de5MHR7n6uqKs0FBMsdj3bp1JPrZM3z48AFmZmYoKCyErq4urktx9tXU1ER1dTW2bN2KAQMGfBEn9cOHD5OLFy9Sx6XzYWFhgbnz5n12Ss7x48YRaeltGYbBo0ePMGzYMHh5eWHFypUMACz88UeiraODWbNmiTihU9HuOjg4MJ07dSLCL4S4jsO1UyfcuHlT5Fg2BZ2QiYmJRHjU1ClTJMz4ZmZmMDQ0hPBW+O7du7h79y5OnzpFRo4aJVJHWmoqmTJlCj5F+AENPmDifmCyUFlZiXVr18JYiG/w48eP1MIPgIQhgo/Xr1+TqVOmIPLePWbZsmXw6NEDy5ctQ3hYGGbMnImPtbXYt2+fiCL8xo0biI+PJ+PGjkV1dTU6urqiproaQWfP4lxQECIjI4k0H8zAwEBy9MgRxArpU7kQHhYmYPblCz53d3dBoqYyNCTjVlZWFuSrAP5K13nz5k0yQA6hxUdRURF+/fVX2ApZyWtkJIAXR2hjn+fm5BBaIg1hfPz4UeCQLgxaJm+gwRuCP2Gxnefrlwf074/Zs2fjY20tdHR1mVcvX5KWrVrB18eHNfcF/32gZbemwf59+6jCJMWRlpaG95Q+xVzg8ngghAjIUI4cOYIeHh7EyckJDx48QFpaGsSTt1H3ipeMTG1s293+AwZAX19f7nrZdEkZGRlg0wMCwEYWws/S0lKRNJ7yQtgPjU9FJYx+/fqJCDphCDNxmJubM76UvmFcKC8vh6KiIh4+fEiGDx+OGdOnC1Yo165dw8lTp6CkpAS7xixk4eHhZOCgQbh9+zY6duyI7u7uSE5KEggKQghSOXK5nD17llr48cEXAN7e3ti2datElrr/7t+PPbt3i8Rk83VF3bp1g4GQG86QIUNEDF9KSkrw8/OTqu8SVnR36NBBZiJ6NhibmDBuXboIftvZ2eHqtWsiwsPb21sqpZdwG3g8HnUuDxpEPXmC7Oxs0qZtW0ZDQ4PhC0pbW1ucPnWKU01lZm4Of3//LxaD/TmpNdtQcmtywZqCgouvGkpNTUVISIjAYKQi5p1CLQD7yfCxcmBJyMPj8RguMlAej4fJQtY1Pmh0e3yoqKiwMuq2aduWMaVIBi7oCKGXXEVFBb8uW4Y7oaHYsGEDevv4wN7eHr59+sDPzw9r1q7Fnj/+YFxZXIRUVFXhLKZzHCuDK08YSlJyYeTm5iI1NRXfjB4tIph+++033Llzh4mIiMCYMWMESY3OnzsH7169sHvXLmzduhVz5sxhPD09BdtlbW1tTr85HyGuRhpoaWnB0dGxoQ+EXjIejyf1mYC/CFI1NDSY23fu4E5oKBYuWgRfX184t2+Pvn37wsfXF9t37MDuPXsYWxYmFAMDA9jb24t84GPkeIeE848cPnwYd0JDcejQIfTq1QvW1tbo06cPBgwciIULF+LAwYNSJ7TOYoJBFkeiOLhyz3j16sWw7SQKi4pQU1ODCxcv4pdff2UtKy3h+KdiwIABn1RORVUVfCKTz4GyjHwxZhw5isQNunSZZwB4enoy/n5+pLCwEPr6+jAwNBRkQfPz80PXbt1YZ5iRo0Yx+/buFeT/UFNTg529PRISEjBnzhxYWVlJlBs2bBizatUqcvjQIXz8+BF6enrQ0tJCdnY2ampqYGFhgeLiYpSVlaF58+bYvHkzDh8+LHHvX375RcRVRVNTEwYGBmjWvDksLCxgYWEBGxsbtGrVCo6OjkxxcTFJTk6GpaUllJSUsHvXLixeskSifbsbXXDY+PLmzZ0LcWKFyooKGBkZQUdHR/DHY4nuUFFRQb9+/dCbRfiEhYVBXV0dlZWVMDAwgIODA3r07Am+246enp5IZRMnTWqIf1VRwYdGa2mnzp0xbfp08Hg89OvblzNL2OQpU5gtmzeTP//8EwUFBVBSUgIhBEZGRjAwMBBMGAUFBSguLsaWrVsFxA42NjbIzMyEp5cXVq1ahYU//ghdXV2o83jIyc5GVnY2aqqrYWJigjFjxuDXxg+3qqoKIZcvY/acORLt2r9/v6DPxXnkFi9ejOFiH3lVVRVMTExE+pwtM5m6mhqGBgQInGfV1dWZX3/5haz87TcGaEjPKA62cR83bhzEQ9vKy8thaGgIbaE2aGpqSoy7spIS3D08wHehkga+qigvL49s2bwZs+fMwYoVK5CYkICjR4+iS5cuzJLFi8nJkycFZTQ1NaH/hZ2QvXr1YiZNnEiE1TVKSkpQ5/HAU1cHj8eDiooKGIbBhw8fkJGRgdraWixYsOCzSCD4sLW1xTfffIMePXpARUUFjxvVVcLqHzbjnb6+PkaOHCnQPwOURpB/ClVVVaSmpkYk4bYwc4uw35005OfnE2Ulpa+SErCgoIDk5OSgsLAQiQkJsLO3R5cuXb5qn3Lpib4WSktLCcMwMj9QPi5dukTq6+owaPDgL97OnJwcUlBQgNzcXCQnJ8PFxQXOzs5/a3+UlJSQjIwMlJaW4v27dzAzM4NXr15/axtyc3KIsYkJk5WVRfR0dUXYU0JCQoiGhgYsLS3RokWLr9au3NxcoqqqClmx7MA/8942oQlNaEITmtCEJjShCU1oQhOa0IQmNKEJTWhCE5rQhCY0oQlNaEITmtCEJjShCf9PQO2Xc/DQQSKNZru9c3t0k+IILY4DBw4QPX09DB0yVG6foCdPnpDnL56joqICBgYG6Na1G7iosAAgIyODXAy+KPX8kCFD0LyZ9FSN2TnZ5Ny5c3BycoKHuwdVm2NiY0hUVBRKS0uhq6uLzp06o3Xr1nI977Nnz8jDRw8xcMBAmJubU5d98PABiY6OxqCBg2BmZvZV/a7OnDlD8gvYE/zMmM6d0jDwbCDJz8/HsIBhAuKI3NxccjboLIyNjTEsgDtgPiEhgVy/8RffJMMw0NTUhGtHVzg6OspOr5qWRi5dvoSOHTvCrbP8KTLLy8tJeHg4EpMSQQiBlZUVPHt6UvnEAcDuPbuJiYkJAoYGcF5/+fJlkprGHrLYvHlzDBk8hOp+F4MvktzcXEyZPIXq+levXpHwiHCp5ydOmAh1jsxt8W/jye3bt+Hh7gEnJyeqe967d4+8fPUSlZWVMDIygoeHB6wsrajKBgcHk4zMDIwYPgIGBgaCMtHR0eTBwwfo49uHVVZQR4JUVVXhQ9UH1NU3ZClTUVGBnm6Dh3lNLV3Qd9ybOHLo0CEwDIOioiIiHr3AhUuXLpHAs4GCFz0zMxMvX77E8+fPSfv27aXWU1dXh6rKhpwelVWVKCsrg7a2NtTVGqJY6uu4qcOrq6uRnJwMM1Mz0CA8PJwcb2SX1tLSQlZWFl6/fo27d+8SDw86AQoAEXcjkJmZiUePH9EWAQAUFhQiOTn5b8kJkZGZgaysLJnx3mxwae+Cffv34XLIX0miLodcRnJyMvr4yo6drqioQHJyMng8HtTU1EAIQUpKCmJjY3H9+nXSp08fzr6urKpEcnIybFvITjLOUpbs2LEDBQUFUFVVhYKCAtLT0xETE4Pi4mJCE+2QnJws890DgOqaasH7m5ffkODLyLAh1pw2929paSlZs3YN6uvrERsbS2gE0se6j4L7lpWXobKyEvr6+lBWaghzJOAm+CgvK0dycjKc29FR0Z08dZJcDL4IBQUFaGhoICsrCy9fvsTr168JzeIhKzsLSUlJCDonmpGypKQEycnJUmnNqAXgzBkzBdEXv636Dba2tpg4YaJcM2dUVBQ0NDRQWVmJp8+eUpcrLCok69evh66uLqZ9Pw36+vpMSmoK2bdvH17HveYsK8x9d//BfXLhwgX07dMXro0JwBcsWCDPI8jEjZs3oK6ujmnTpqF5s+ZMbm4u2fPHHpntFEZmVibZtm0bNDU1pRJA/FugpKSExYsWy72CatmyJXPq9Cny7NkzvH37lhBCcODgAXTs2FHmql4Ynp6e8OzZkBO2pKSE/L79d4SFh33VZ37w4AEKCgrQuVNnAbVTSEgICY8Ix53QO59bvQiEV4hr1q4hHz9+xILGVJC0eBb9DPX19dDQ0EDU0yiqMs7t/oquCQ4OJpH3IjFq1ChYW1l/8e8mLS2N7Ni5A82bN8eUyVOgoaGB+Ph4HDp8CJcuy05tK4z379/j4aOHpIsbXUTWl+PIkYGKigry+vVrtG/fHlZWVhLxnFxISUkBIQRdunQRkG5aWVoxPy35Cd+M/uZfE16TkJBAamtr4eLiIthWGxsbM/9Z8B98P/V76nZGRUVBQUEBAwYMwIcPHxAdHf3Vczv8E/D384e6ujouXb6ES5cvgcfjwd+PLqkQG3R0dJhff/mVqaurQ0FBwVfrs+SkZACAj4/PX8/i788wDIOkpKS/rwMp8TTqKSwtLdGhQwfEx8ejtLT0X/U+JSU39Jm7u7sgj469vT1sbGxQUFAgV3sNDAwQEhKCouIiqjJ/mwCMfh6Nuro6OLV1Qtu2bVFQUIDExESqRtZUN2yxxZMM8YPv/y2ormnYkmhqiObolbed0dHRsG1hC6e2TlBXV6eetf8J1NfXIzQslAj/5efnU42rlpYW4+/nj5ycHOTm5sLfz1/AZkOL2ppaVFRUkPLycvLq1Svy088/kUbSi6/2bvDHWVzfp6qqKhcH4N+BlNQUkpObg7Zt26Jt27aor69HdHT0P90sEfC38uLf97TvpzHC52kweNBgVFdX49y5c1TXU2+BPxdPnz6FpqYmrKysoKuni8uXL/+rP+x/Ci9fviRHjx1FW6e2UFRURGvH1ngW/Uxunenfhfr6ely9elXkWDOTZtTlbW1tBewon5I57Oatm7h56y8iXmVlZYwYPgK//vKr3HV9LviJ0/9N4O+0nNo6CViVoqL+73539vb2zJkzZ0jU0yg8f/6cFIslrBLH3yIA+TqtFi1aCFIp6ujoICYmhq4C/mf/73q3WJrZ0NDP+Qj4k4KCggLi4uKgoaEBQohcOtO/E0pKSli0UJTzkdYSCgAXLlwQUGtduHhB7vvb2NjA3KyBoFRTUxPO7Z2hr6f/j0wUhBDWBPb/JJ4/fw4tLS3k5OQgJycHxsbGSEhIQGpqKhHWj/+T4H83X+r79vf3R/zbeARfCkanTp04r/1bBCB/xklMTJRI5/gk6gnp5NqJcyA0eA1LY/EcDTGxMaRly5bgqfP+FQPJX8KLt/P169fEwsJCJp1UWVkZWb1mNQAgKEjUmiWPzvTvhjwCTxjRz6PJyZMn4eXphXpSj/DwcJlWfXE4OjoKjCB/F7Q0G7jmMjMziampqcAAs3rNaoGF9t8Afv9++PABh48cFjn3b9p9aWo1qIxy83IFpLrCoMmvLXY98+rVK3Lk6BHcu3eP89q/RQBGR0dDS0sL48eNFxyrrq7GgYMHqJbjNjY2UFZWxsNHDxEVFUUsLS3x8tVLHD9+HJYWljLL/12wtLRkVv62ksTExiDyXiSxa2WHhMQEHD12FDo6OjLL8611Pr19BNT2AHA38i5iYmKQmJRIWtjQ8buVlpVCXBfHlej8U0EIAZvOT9a9KioqyOYtm6GtrY1+/foxAPDbqt9I8KVgVFRUkL9Lv1tVVSXRfjU1NU5dpKOjI2JfxiIoKAipqalEUVERp880pNl0cHT4O5pNhadRDZPmpImTRPKV/Hniz3+Vd4G9nT0UFBQQFhYGQwNDGBsb40nUEyxctJBYW1uDx5N/gdOmTRvm5KmTRJa+86sLQL5Oq4dHDwn257379pKEhATk5+cTrg9GQ0ODiYqKIoFnA3Em8IzguLq6OgYNGoRZQsmy/2kMHz4cx44dQ7BQ4h9lZWUEDA3AksVLOMs+ffoUSkpK6O7eXWRVm5CQQGJiYuTS3QizAvMRExtD2jm1+6KCpa6uDhs2bpC73JUrV1BeXo7Ro0dj6c8N+Zb9/f1x6tQpXLl65Us2kRP3H9zH/Qf3RY51EcoLwgZXV1fm2PFjJDY2Fjt37RQct7a2hk9vn3/FbqSouIisW7cONjY2cHBwEGnT1WtXSWhoqNyr7a8FPT095v6D++TixYs4euyvFLiampoYOmQoZkyf8Un1DhwwEO/evRNhihaH3AJQS0uLuXX7FqFd6isqKcLX1xcu7SWT1Pj6+iIhIYHKadfV1ZXJzc0VeIob6BugXbt2cllYLS0s4evrC1Mz+lwhujq68PX1lZq7WByODo5MYVEhiY2NRVlpGXR0deDczlmCJp8N7dq1g66OrsSW3tbWlgkNDSVKyrKHy87ODqpq7Em55TFO0KBb124oK2dP+7hhPbdQ1NfXR//+/eHS3kXwrB1cOjARdyNIbY3srG4mJibw9fWFtbX1J7Xd0MAQvr6+rOf4OkUujBs7jomPjydJSUmoJ/WwMLegjngAGt59ml2BMHr26In6etnO0wBQVVkFHx8fVsOSW2c3KCsrQ0VFhaouewd78DR4gsAHGpiamsLX15c1fQAbunXtxmRnZ5NXr16hqqoKBoYGcHZ2plZvdXLtBFtbW5H3TkNDg0lKSiIJiQkwMTGRq6+b0IQmNKEJTWhCE5rwfxX/A8MuT6H0ty2PAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDE2LTA1LTIwVDE1OjQ4OjUzKzAyOjAwEhGlUwAAACV0RVh0ZGF0ZTptb2RpZnkAMjAxNi0wNS0yMFQxNTo0ODo1MyswMjowMGNMHe8AAAAASUVORK5CYII=';
    pdf.addImage(imgData, 'PNG', 120, 300, 320, 57);
    pdf.setFont("helvetica", "bold");
    pdf.setFontSize(40);
    pdf.setTextColor(89, 89, 89);
    pdf.text(190,420,"Reporting");
    pdf.setTextColor(0,102,204);
    pdf.setFont("helvetica", "normal");
    pdf.setFontSize(20);
    pdf.addPage();
}

function newTab(id,contentID,tabName){
    var list_item=document.createElement('li');
    list_item.setAttribute("role", "presentation");
    var ref=document.createElement('a');
    ref.setAttribute("id",id);
    ref.setAttribute("href",contentID);
    ref.setAttribute("role", "tab");
    ref.setAttribute("data-toggle", "tab");
    ref.setAttribute("onclick", "changeTab('"+contentID+"')");
    var text=document.createTextNode(tabName);
    ref.appendChild(text);
    list_item.appendChild(ref);
    $('#warBerry_tabs').append(list_item);
    var newtabcontent=document.createElement('div');
    newtabcontent.setAttribute("role", "tabpanel");
    newtabcontent.className="tab-pane";
    newtabcontent.setAttribute("id", contentID.split("#")[1]);
    $('#content-tabs').append(newtabcontent);
}

function changeTab(id){
    var net_scan=document.getElementById("network_scanner_content");
    net_scan.innerHTML="";
    var previous_item=localStorage.getItem("previous");
    document.getElementById(previous_item).setAttribute("style","display:none");
    var id_c=id.split('#')[1];
    localStorage.setItem("previous", id_c);
    document.getElementById(id_c).setAttribute("style","visibility:visible");
}

function changeResponderTab(id){
    var pre=localStorage.getItem("previousResponder");
    document.getElementById(pre).className="tab-pane";
    var id_content=id.split("#")[1];
    localStorage.setItem("previousResponder", id_content);
    var active_pane=document.getElementById(id_content);
    active_pane.className="tab-pane active";
}

function filePresentation(lines){
    var resolved=lines.length-1;
    var table=document.createElement('table');
    var tbody=document.createElement('tbody');
    if (resolved==0){
        var row=document.createElement('tr');
        table.className="table";
        var column=document.createElement('td');
        column.className="warning";
        var column_text=document.createTextNode("No Results Found");
        column.appendChild(column_text);
        row.appendChild(column);
        tbody.appendChild(row);
    }
    else {
        table.className="table table-striped";
        if (resolved>11){
            var line_items= [];
            $.each(lines, function (n, elem) {
                if (n!=resolved) {
                    line_items.push(elem);
                }
            });
            for (var i=0; i<line_items.length; i++){
                if (i%4==0){
                    var row=document.createElement('tr');
                    var column1=document.createElement('td');
                    var column2=document.createElement('td');
                    var column3=document.createElement('td');
                    var column4=document.createElement('td');
                    var column1_text=document.createTextNode(line_items[i]);
                    column1.appendChild(column1_text);
                    if ((i+1)<line_items.length) {
                        var column2_text = document.createTextNode(line_items[i + 1]);
                    }
                    else{
                        var column2_text = document.createTextNode("-");
                    }
                    column2.appendChild(column2_text);
                    if ((i+2)<line_items.length) {
                        var column3_text = document.createTextNode(line_items[i + 2]);
                    }
                    else{
                        var column3_text = document.createTextNode("-");
                    }
                    column3.appendChild(column3_text);
                    if ((i+3)<line_items.length) {
                        var column4_text = document.createTextNode(line_items[i + 3]);
                    }
                    else{
                        var column4_text = document.createTextNode("-");
                    }
                    column4.appendChild(column4_text);
                    row.appendChild(column1);
                    row.appendChild(column2);
                    row.appendChild(column3);
                    row.appendChild(column4);
                    tbody.appendChild(row);
                }
            }
        }
        else {
            $.each(lines, function (n, elem) {
                if (n!=resolved) {
                    var row = document.createElement('tr');
                    var column = document.createElement('td');
                    var cell_text = document.createTextNode(elem);
                    column.appendChild(cell_text);
                    row.appendChild(column);
                    tbody.appendChild(row);
                }
            });
        }
    }
    table.appendChild(tbody);
    return table;
}

function enum_presentation(lines){
    var resolved=lines.length-1;
    var table=document.createElement('table');
    var tbody=document.createElement('tbody');
    if (resolved==2){
        var row=document.createElement('tr');
        table.className="table";
        var column=document.createElement('td');
        column.className="warning";
        var column_text=document.createTextNode("No Results Found");
        column.appendChild(column_text);
        row.appendChild(column);
        tbody.appendChild(row);
    }
    else {
        table.className = "table table-striped";
        var line_items = [];

        $.each(lines, function (n, elem) {
            if (n != resolved) {
                line_items.push(elem);
            }
        });

        var table_h=document.createElement('thead');
        var t_row=document.createElement('tr');
        var ht1=document.createElement('th');
        var ht2=document.createElement('th');
        var ht3=document.createElement('th');
        var ht1_text=document.createTextNode("Host");
        var ht2_text=document.createTextNode("Port");
        var ht3_text=document.createTextNode("Service");
        ht1.appendChild(ht1_text);
        ht2.appendChild(ht2_text);
        ht3.appendChild(ht3_text);
        t_row.appendChild(ht1);
        t_row.appendChild(ht2);
        t_row.appendChild(ht3);
        table_h.appendChild(t_row);
        table.appendChild(table_h);

        var ports = [];
        var port_details = [];
        var host_details = [[]];
        var ports_counter = 0;
        var host_counter = 0;
        for (var i = 0; i < line_items.length; i++) {
            if ((line_items[i].indexOf("report") > 0)) {
                var hostname = line_items[i].split(' ')[4];
                if (host_counter != 0) {
                    host_details[host_counter - 1]['ports'] = ports;
                    var ports = [];
                }
                else {
                    host_details[host_counter]['hostname'] = hostname;
                }
                host_counter++;
                var ports = [];
                ports_counter = 0;
            }
            else if (line_items[i].indexOf(" open") > 0) {
                var port = line_items[i].split(' ')[0];
                var service=line_items[i].split('open ')[1];
                port_details['port'] = port;
                port_details['service']=service;
                ports[ports_counter] = port_details;
                ports_counter++;
            }
        }
        host_details[host_counter - 1]['ports'] = ports;

        for (var i = 0; i < host_details.length; i++) {
            for (var j = 0; j < host_details[i]['ports'].length; j++) {
                var row = document.createElement('tr');
                var host = document.createElement('td');
                var portname = document.createElement('td');
                var http_t = document.createElement('td');
                var host_text = document.createTextNode(host_details[i]['hostname']);
                var portname_text = document.createTextNode(host_details[i]['ports'][j]['port']);
                var http_ttext = document.createTextNode(host_details[i]['ports'][j]['service']);
                host.appendChild(host_text);
                portname.appendChild(portname_text);
                http_t.appendChild(http_ttext);
                row.appendChild(host);
                row.appendChild(portname);
                row.appendChild(http_t);
                tbody.appendChild(row);
            }
        }
    }
    table.appendChild(tbody);
    return table;
}

function waf_presentation(lines){
    var resolved=lines.length-1;
    var table=document.createElement('table');
    var tbody=document.createElement('tbody');
    if (resolved==2){
        var row=document.createElement('tr');
        table.className="table";
        var column=document.createElement('td');
        column.className="warning";
        var column_text=document.createTextNode("No Results Found");
        column.appendChild(column_text);
        row.appendChild(column);
        tbody.appendChild(row);
    }
    else {
        table.className = "table table-striped pre-scrollable";
        var line_items = [];
        $.each(lines, function (n, elem) {
            if (n != resolved) {
                line_items.push(elem);
            }
        });

        var table_h=document.createElement('thead');
        var t_row=document.createElement('tr');
        var ht1=document.createElement('th');
        var ht2=document.createElement('th');
        var ht3=document.createElement('th');
        var ht1_text=document.createTextNode("Host");
        var ht2_text=document.createTextNode("Port");
        var ht3_text=document.createTextNode("WAF Detection");
        ht1.appendChild(ht1_text);
        ht2.appendChild(ht2_text);
        ht3.appendChild(ht3_text);
        t_row.appendChild(ht1);
        t_row.appendChild(ht2);
        t_row.appendChild(ht3);
        table_h.appendChild(t_row);
        table.appendChild(table_h);

        var ports = [];
        var port_details = [];
        var host_details = [[]];
        var ports_counter = 0;
        var host_counter = 0;
        for (var i = 0; i < line_items.length; i++) {
            if ((line_items[i].indexOf("scan report for") > 0)) {
                var hostname = line_items[i].split(' ')[4];
                if (host_counter != 0) {
                    host_details[host_counter - 1]['ports'] = ports;
                }
                else {
                    host_details[host_counter]['hostname'] = hostname;
                }
                host_counter++;
                var ports = [];
                ports_counter = 0;
            }
            else if (line_items[i].indexOf(" open") > 0) {
                var port = line_items[i].split(' ')[0];
                port_details['port'] = port;
                if (line_items[i+1].indexOf("http-waf-detect")>0) {
                    var waf_title = line_items[i].split(": ")[1];
                    port_details['waf-detect'] = waf_title;
                }
                else{
                    port_details['waf-detect'] = "-";
                }
                ports[ports_counter] = port_details;
                ports_counter++;
            }
        }
        host_details[host_counter - 1]['ports'] = ports;

        for (var i = 0; i < host_details.length; i++) {
            for (var j = 0; j < host_details[i]['ports'].length; j++) {
                var row = document.createElement('tr');
                var host = document.createElement('td');
                var portname = document.createElement('td');
                var waf_title = document.createElement('td');
                var host_text = document.createTextNode(host_details[i]['hostname']);
                var portname_text = document.createTextNode(host_details[i]['ports'][j]['port']);
                var waf_ttext = document.createTextNode(host_details[i]['ports'][j]['waf-detect']);
                host.appendChild(host_text);
                portname.appendChild(portname_text);
                waf_title.appendChild(waf_ttext);
                row.appendChild(host);
                row.appendChild(portname);
                row.appendChild(waf_title);
                tbody.appendChild(row);
            }
        }
    }
    table.appendChild(tbody);
    return table;
}

function nfs_presentation(lines){
    var resolved=lines.length-1;
    var table=document.createElement('table');
    var tbody=document.createElement('tbody');
    if (resolved==2){
        var row=document.createElement('tr');
        table.className="table";
        var column=document.createElement('td');
        column.className="warning";
        var column_text=document.createTextNode("No Results Found");
        column.appendChild(column_text);
        row.appendChild(column);
        tbody.appendChild(row);
    }
    else {
        table.className = "table table-striped pre-scrollable";
        var line_items = [];
        $.each(lines, function (n, elem) {
            if (n != resolved) {
                line_items.push(elem);
            }
        });
        var table_h=document.createElement('thead');
        var t_row=document.createElement('tr');
        var ht1=document.createElement('th');
        var ht2=document.createElement('th');
        var ht3=document.createElement('th');
        var ht1_text=document.createTextNode("Host");
        var ht2_text=document.createTextNode("Port");
        var ht3_text=document.createTextNode("NFS Path");
        ht1.appendChild(ht1_text);
        ht2.appendChild(ht2_text);
        ht3.appendChild(ht3_text);
        t_row.appendChild(ht1);
        t_row.appendChild(ht2);
        t_row.appendChild(ht3);
        table_h.appendChild(t_row);
        table.appendChild(table_h);

        var ports = [];
        var port_details = [];
        var host_details = [[]];
        var ports_counter = 0;
        var host_counter = 0;
        for (var i = 0; i < line_items.length; i++) {
            if ((line_items[i].indexOf("scan report") > 0)) {
                var hostname = line_items[i].split(' ')[4];
                if (host_counter != 0) {
                    host_details[host_counter - 1]['ports'] = ports;
                }
                else {
                    host_details[host_counter]['hostname'] = hostname;
                }
                host_counter++;
                var ports = [];
                ports_counter = 0;
            }
            else if (line_items[i].indexOf(" open") > 0) {
                var port = line_items[i].split(' ')[0];
                port_details['port']=port;
                if (line_items[i+1].indexOf("nfs-showmount")>0) {
                    var nfspath = line_items[i + 1];
                    if (nfspath.indexOf('/') > 0) {
                        port_details['nfs-path'] = nfspath;
                    }
                    else {
                        port_details['nfs-path']="-";
                    }
                }
                else{
                    port_details['nfs-path']="-";
                }
                ports[ports_counter] = port_details;
                ports_counter++;
            }
        }

        host_details[host_counter - 1]['ports'] = ports;
        for (var i = 0; i < host_details.length; i++) {
            for (var j = 0; j < host_details[i]['ports'].length; j++) {
                var row = document.createElement('tr');
                var host = document.createElement('td');
                var portname = document.createElement('td');
                var path_t = document.createElement('td');
                var host_text = document.createTextNode(host_details[i]['hostname']);
                var portname_text = document.createTextNode(host_details[i]['ports'][j]['port']);
                var path = document.createTextNode(host_details[i]['ports'][j]['nfs-path']);
                host.appendChild(host_text);
                portname.appendChild(portname_text);
                path_t.appendChild(path);
                row.appendChild(host);
                row.appendChild(portname);
                row.appendChild(path_t);
                tbody.appendChild(row);
            }
        }
    }
    table.appendChild(tbody);
    return table;
}

function http_title_presentation(lines){
    var resolved=lines.length-1;
    var table=document.createElement('table');
    var tbody=document.createElement('tbody');
    if (resolved==0){
        var row=document.createElement('tr');
        table.className="table";
        var column=document.createElement('td');
        column.className="warning";
        var column_text=document.createTextNode("No Results Found");
        column.appendChild(column_text);
        row.appendChild(column);
        tbody.appendChild(row);
    }
    else {
        table.className = "table table-striped pre-scrollable";
        var line_items = [];
        $.each(lines, function (n, elem) {
            if (n != resolved) {
                line_items.push(elem);
            }
        });

        var table_h=document.createElement('thead');
        var t_row=document.createElement('tr');
        var ht1=document.createElement('th');
        var ht2=document.createElement('th');
        var ht3=document.createElement('th');
        var ht1_text=document.createTextNode("Host");
        var ht2_text=document.createTextNode("Port");
        var ht3_text=document.createTextNode("HTTP - Title");
        ht1.appendChild(ht1_text);
        ht2.appendChild(ht2_text);
        ht3.appendChild(ht3_text);
        t_row.appendChild(ht1);
        t_row.appendChild(ht2);
        t_row.appendChild(ht3);
        table_h.appendChild(t_row);
        table.appendChild(table_h);

        var ports = [];
        var port_details = [];
        var host_details = [[]];
        var ports_counter = 0;
        var host_counter = 0;
        for (var i = 0; i < line_items.length; i++) {
            if ((line_items[i].indexOf("report") > 0)) {
                var hostname = line_items[i].split(' ')[4];
                if (host_counter != 0) {
                    host_details[host_counter - 1]['ports'] = ports;
                }
                else {
                    host_details[host_counter]['hostname'] = hostname;
                }
                host_counter++;
                var ports = [];
                ports_counter = 0;
            }
            else if (line_items[i].indexOf(" open") > 0) {
                var port = line_items[i].split(' ')[0];
                port_details['port'] = port;
            }
            else if (line_items[i].indexOf("http-title")>0){
                var http_title=line_items[i].split(": ")[1];
                port_details['http-title']=http_title;
                ports[ports_counter] = port_details;
                ports_counter++;
            }
        }
        host_details[host_counter - 1]['ports'] = ports;

        for (var i = 0; i < host_details.length; i++) {
            for (var j = 0; j < host_details[i]['ports'].length; j++) {
                var row = document.createElement('tr');
                var host = document.createElement('td');
                var portname = document.createElement('td');
                var http_t = document.createElement('td');
                var host_text = document.createTextNode(host_details[i]['hostname']);
                var portname_text = document.createTextNode(host_details[i]['ports'][j]['port']);
                var http_ttext = document.createTextNode(host_details[i]['ports'][j]['http-title']);
                host.appendChild(host_text);
                portname.appendChild(portname_text);
                http_t.appendChild(http_ttext);
                row.appendChild(host);
                row.appendChild(portname);
                row.appendChild(http_t);
                tbody.appendChild(row);
            }
        }
    }
    table.appendChild(tbody);
    return table;
}

function mysql_presentation(lines){
    var resolved=lines.length-1;
    var table=document.createElement('table');
    var tbody=document.createElement('tbody');
    if (resolved==2){
        var row=document.createElement('tr');
        table.className="table";
        var column=document.createElement('td');
        column.className="warning";
        var column_text=document.createTextNode("No Results Found");
        column.appendChild(column_text);
        row.appendChild(column);
        tbody.appendChild(row);
    }
    else {
        table.className = "table table-striped pre-scrollable";
        var line_items = [];
        $.each(lines, function (n, elem) {
            if (n != resolved) {
                line_items.push(elem);
            }
        });

        var table_h = document.createElement('thead');
        var t_row = document.createElement('tr');
        var ht1 = document.createElement('th');
        var ht2 = document.createElement('th');
        var ht3 = document.createElement('th');
        var ht1_text = document.createTextNode("Host");
        var ht2_text = document.createTextNode("Port");
        var ht3_text = document.createTextNode("Accounts");
        ht1.appendChild(ht1_text);
        ht2.appendChild(ht2_text);
        ht3.appendChild(ht3_text);
        t_row.appendChild(ht1);
        t_row.appendChild(ht2);
        t_row.appendChild(ht3);
        table_h.appendChild(t_row);
        table.appendChild(table_h);

        var ports = [];
        var port_details = [];
        var host_details = [[]];
        var ports_counter = 0;
        var host_counter = 0;
        for (var i = 0; i < line_items.length; i++) {
            if ((line_items[i].indexOf("scan report") > 0)) {
                var hostname = line_items[i].split(' ')[4];
                if (host_counter != 0) {
                    host_details[host_counter - 1]['ports'] = ports;
                }
                else {
                    host_details[host_counter]['hostname'] = hostname;
                }
                host_counter++;
                var ports = [];
                ports_counter = 0;
            }
            else if (line_items[i].indexOf(" open") > 0) {
                var port = line_items[i].split(' ')[0];
                port_details['port'] = port;
            }
            else if (line_items[i].indexOf(" Accounts")>0){
                var accounts_all=[];
                var accounts = line_items[i+1];
                if (accounts.indexOf(" No valid accounts found")>0) {
                    port_details['accounts']=[];
                    ports[ports_counter] = port_details;
                    ports_counter++;
                    console.log[host_details];
                }
                else{
                    var end_c;
                    for (var j=i+2; j<line_items.length; j++){
                        if (line_items[j].indexOf(" Statistics")){
                            end_c=j-1;
                        }
                    }
                    for (var j=i+1; j<=end_c; j++){
                        var ac=line_items[j];
                        accounts_all.push(ac);
                    }
                    port_details['accounts']=accounts_all;
                    ports[ports_counter] = port_details;
                    ports_counter++;
                }
            }
         }
        host_details[host_counter - 1]['ports'] = ports;
        for (var i = 0; i < host_details.length; i++) {
            for (var j = 0; j < host_details[i]['ports'].length; j++) {
                var row = document.createElement('tr');
                var host = document.createElement('td');
                var portname = document.createElement('td');
                var accounts = document.createElement('td');
                var host_text = document.createTextNode(host_details[i]['hostname']);
                var portname_text = document.createTextNode(host_details[i]['ports'][j]['port']);
                var acc_t="";
                if (host_details[i]['ports'][j]['accounts'].length==0){
                    acc_t="-"
                }
                else{
                    for (var k=0; k<host_details[i]['ports'][j]['accounts'].length; k++){
                        acc_t=acc_t+host_details[i]['ports'][j]['accounts'][k]+'\n';
                    }
                }
                var accounts_ttext = document.createTextNode(acc_t);
                host.appendChild(host_text);
                portname.appendChild(portname_text);
                accounts.appendChild(accounts_ttext);
                row.appendChild(host);
                row.appendChild(portname);
                row.appendChild(accounts);
                tbody.appendChild(row);
            }
        }
    }
    table.appendChild(tbody);
    return table;
}

function snmp_presentation(lines){
    var resolved=lines.length-1;
    var table=document.createElement('table');
    var tbody=document.createElement('tbody');
    if (resolved==2){
        var row=document.createElement('tr');
        table.className="table";
        var column=document.createElement('td');
        column.className="warning";
        var column_text=document.createTextNode("No Results Found");
        column.appendChild(column_text);
        row.appendChild(column);
        tbody.appendChild(row);
    }
    else {
        table.className = "table table-striped pre-scrollable";
        var line_items = [];
        $.each(lines, function (n, elem) {
            if (n != resolved) {
                line_items.push(elem);
            }
        });

        var table_h=document.createElement('thead');
        var t_row=document.createElement('tr');
        var ht1=document.createElement('th');
        var ht2=document.createElement('th');
        var ht3=document.createElement('th');
        var ht1_text=document.createTextNode("Host");
        var ht2_text=document.createTextNode("Port");
        var ht3_text=document.createTextNode("SNMP Enterprise");
        ht1.appendChild(ht1_text);
        ht2.appendChild(ht2_text);
        ht3.appendChild(ht3_text);
        t_row.appendChild(ht1);
        t_row.appendChild(ht2);
        t_row.appendChild(ht3);
        table_h.appendChild(t_row);
        table.appendChild(table_h);

        var ports = [];
        var port_details = [];
        var host_details = [[]];
        var ports_counter = 0;
        var host_counter = 0;
        for (var i = 0; i < line_items.length; i++) {
            if ((line_items[i].indexOf("scan report for") > 0)) {
                var hostname = line_items[i].split(' ')[4];
                if (host_counter != 0) {
                    host_details[host_counter - 1]['ports'] = ports;
                }
                else {
                    host_details[host_counter]['hostname'] = hostname;
                }
                host_counter++;
                var ports = [];
                ports_counter = 0;
            }
            else if (line_items[i].indexOf(" open") > 0) {
                var port = line_items[i].split(' ')[0];
                port_details['port'] = port;
                if (line_items[i+1].indexOf("snmp-info")>0) {
                    if (line_items[i+2].indexOf("enterprise")>0){
                        var enterprise_title = line_items[i].split(": ")[1];
                        port_details['enterprise'] = enterprise_title;
                    }
                }
                else{
                    port_details['enterprise'] = "-";
                }
                ports[ports_counter] = port_details;
                ports_counter++;
            }
        }
        host_details[host_counter - 1]['ports'] = ports;

        for (var i = 0; i < host_details.length; i++) {
            for (var j = 0; j < host_details[i]['ports'].length; j++) {
                var row = document.createElement('tr');
                var host = document.createElement('td');
                var portname = document.createElement('td');
                var waf_title = document.createElement('td');
                var host_text = document.createTextNode(host_details[i]['hostname']);
                var portname_text = document.createTextNode(host_details[i]['ports'][j]['port']);
                var waf_ttext = document.createTextNode(host_details[i]['ports'][j]['enterprise']);
                host.appendChild(host_text);
                portname.appendChild(portname_text);
                waf_title.appendChild(waf_ttext);
                row.appendChild(host);
                row.appendChild(portname);
                row.appendChild(waf_title);
                tbody.appendChild(row);
            }
        }
    }
    table.appendChild(tbody);
    return table;
}

function ftp_presentation(lines){
    var resolved=lines.length-1;
    var table=document.createElement('table');
    var tbody=document.createElement('tbody');
    if (resolved==2){
        var row=document.createElement('tr');
        table.className="table";
        var column=document.createElement('td');
        column.className="warning";
        var column_text=document.createTextNode("No Results Found");
        column.appendChild(column_text);
        row.appendChild(column);
        tbody.appendChild(row);
    }
    else {
        table.className = "table table-striped pre-scrollable";
        var line_items = [];
        $.each(lines, function (n, elem) {
            if (n != resolved) {
                line_items.push(elem);
            }
        });

        var table_h=document.createElement('thead');
        var t_row=document.createElement('tr');
        var ht1=document.createElement('th');
        var ht2=document.createElement('th');
        var ht3=document.createElement('th');
        var ht1_text=document.createTextNode("Host");
        var ht2_text=document.createTextNode("Port");
        var ht3_text=document.createTextNode("FTP Anon");
        ht1.appendChild(ht1_text);
        ht2.appendChild(ht2_text);
        ht3.appendChild(ht3_text);
        t_row.appendChild(ht1);
        t_row.appendChild(ht2);
        t_row.appendChild(ht3);
        table_h.appendChild(t_row);
        table.appendChild(table_h);

        var ports = [];
        var port_details = [];
        var host_details = [[]];
        var ports_counter = 0;
        var host_counter = 0;
        for (var i = 0; i < line_items.length; i++) {
            if ((line_items[i].indexOf("scan report for") > 0)) {
                var hostname = line_items[i].split(' ')[4];
                if (host_counter != 0) {
                    host_details[host_counter - 1]['ports'] = ports;
                }
                else {
                    host_details[host_counter]['hostname'] = hostname;
                }
                host_counter++;
                var ports = [];
                ports_counter = 0;
            }
            else if (line_items[i].indexOf(" open") > 0) {
                var port = line_items[i].split(' ')[0];
                port_details['port'] = port;
                if (line_items[i+1].indexOf("ftp-anon:")>0) {
                    var ftp_title = line_items[i].split(": ")[1];
                    port_details['ftp-anon'] = ftp_title;
                }
                else{
                    port_details['ftp-anon'] = "-";
                }
                ports[ports_counter] = port_details;
                ports_counter++;
            }
        }
        host_details[host_counter - 1]['ports'] = ports;

        for (var i = 0; i < host_details.length; i++) {
            for (var j = 0; j < host_details[i]['ports'].length; j++) {
                var row = document.createElement('tr');
                var host = document.createElement('td');
                var portname = document.createElement('td');
                var ftp_title = document.createElement('td');
                var host_text = document.createTextNode(host_details[i]['hostname']);
                var portname_text = document.createTextNode(host_details[i]['ports'][j]['port']);
                var ftp_ttext = document.createTextNode(host_details[i]['ports'][j]['ftp-anon']);
                host.appendChild(host_text);
                portname.appendChild(portname_text);
                ftp_title.appendChild(ftp_ttext);
                row.appendChild(host);
                row.appendChild(portname);
                row.appendChild(ftp_title);
                tbody.appendChild(row);
            }
        }
    }
    table.appendChild(tbody);
    return table;
}

function mssql_presentation(lines){

    var resolved=lines.length-1;
    var table=document.createElement('table');
    var tbody=document.createElement('tbody');
    if (resolved==2){
        var row=document.createElement('tr');
        table.className="table";
        var column=document.createElement('td');
        column.className="warning";
        var column_text=document.createTextNode("No Results Found");
        column.appendChild(column_text);
        row.appendChild(column);
        tbody.appendChild(row);
    }
    else {
        table.className = "table table-striped pre-scrollable";
        var line_items = [];
        $.each(lines, function (n, elem) {
            if (n != resolved) {
                line_items.push(elem);
            }
        });

        var table_h=document.createElement('thead');
        var t_row=document.createElement('tr');
        var ht1=document.createElement('th');
        var ht2=document.createElement('th');
        var ht3=document.createElement('th');
        var ht1_text=document.createTextNode("Host");
        var ht2_text=document.createTextNode("Server");
        var ht3_text=document.createTextNode("Databases");
        ht1.appendChild(ht1_text);
        ht2.appendChild(ht2_text);
        ht3.appendChild(ht3_text);
        t_row.appendChild(ht1);
        t_row.appendChild(ht2);
        t_row.appendChild(ht3);
        table_h.appendChild(t_row);
        table.appendChild(table_h);

        var ports = [];
        var port_details = [];
        var host_details = [[]];
        var ports_counter = 0;
        var host_counter = 0;
        for (var i = 0; i < line_items.length; i++) {
            if ((line_items[i].indexOf("scan report for") > 0)) {
                var hostname = line_items[i].split(' ')[4];
                if (host_counter != 0) {
                    host_details[host_counter - 1]['ports'] = ports;
                }
                else {
                    host_details[host_counter]['hostname'] = hostname;
                }
                host_counter++;
                var ports = [];
                ports_counter = 0;
            }
            else if (line_items[i].indexOf("ms-sql-info") > 0) {
                var server_name = line_items[i+1].split(": ")[1];
                port_details['server-name'] = server_name;
                var end_database_d;
                for (var k=i+1; k<line_items.length; k++){
                    if (line_items[k].indexOf("_  ")){
                        end_database_d=k;
                    }
                }
                var databases=[];
                for (var k=i+1; k<end_database_d; k++){
                    if (line_items[k].indexOf("Instance name:")>0){
                        var database_d=[];
                        var database_n=line_items[k].split(': ')[1];
                        database_d['database-name']=database_n;
                        var db_version=line_items[k+2].split(': ')[1];
                        database_d['version-name']=db_version;
                        databases.push(database_d);
                    }
                }
                port_details['databases-details']=databases;
                ports[ports_counter] = port_details;
                ports_counter++;
            }
        }
        host_details[host_counter - 1]['ports'] = ports;
        console.log(host_details);
        for (var i = 0; i < host_details.length; i++) {
            for (var j = 0; j < host_details[i]['ports'].length; j++) {
                var row = document.createElement('tr');
                var host = document.createElement('td');
                var servername = document.createElement('td');
                var db_details = document.createElement('td');
                var host_text = document.createTextNode(host_details[i]['hostname']);
                var servername_text = document.createTextNode(host_details[i]['ports'][j]['server-name']);
                var db="";
                for (var c=0; c<host_details[i]['ports'][j]['databases-details'].length; c++){
                    db=db+ "Name: "+ host_details[i]['ports'][j]['databases-details'][c]['database-name'];
                    db=db+ " Version: "+host_details[i]['ports'][j]['databases-details'][c]['version-name']+" \n";

                }
                var db_text = document.createTextNode(db);
                host.appendChild(host_text);
                servername.appendChild(servername_text);
                db_details.appendChild(db_text);
                row.appendChild(host);
                row.appendChild(servername);
                row.appendChild(db_details);
                tbody.appendChild(row);
            }
        }
    }
    table.appendChild(tbody);
    return table;
}

function shares_presentation(lines){
    
}

function WifisPresentation(lines){
    var resolved=lines.length-1;
    var table=document.createElement('table');
    var tbody=document.createElement('tbody');
    if (resolved==0){
        var row=document.createElement('tr');
        table.className="table";
        var column=document.createElement('td');
        column.className="warning";
        var column_text=document.createTextNode("No Results Found");
        column.appendChild(column_text);
        row.appendChild(column);
        tbody.appendChild(row);
    }
    else {
        table.className="table table-striped";
        if (resolved>11){
            table.className="table table-striped pre-scrollable";
            var line_items= [];
            $.each(lines, function (n, elem) {
                if (n!=resolved) {
                    var wifi = elem.split(':')[1].split('"')[1];
                    line_items.push(wifi);
                }
            });
            for (var i=0; i<line_items.length; i++){
                if (i%4==0){
                    var row=document.createElement('tr');
                    var column1=document.createElement('td');
                    var column2=document.createElement('td');
                    var column3=document.createElement('td');
                    var column4=document.createElement('td');
                    var column1_text=document.createTextNode(line_items[i]);
                    column1.appendChild(column1_text);
                    if ((i+1)<line_items.length) {
                        var column2_text = document.createTextNode(line_items[i + 1]);
                    }
                    else{
                        var column2_text = document.createTextNode("-");
                    }
                    column2.appendChild(column2_text);
                    if ((i+2)<line_items.length) {
                        var column3_text = document.createTextNode(line_items[i + 2]);
                    }
                    else{
                        var column3_text = document.createTextNode("-");
                    }
                    column3.appendChild(column3_text);
                    if ((i+3)<line_items.length) {
                        var column4_text = document.createTextNode(line_items[i + 3]);
                    }
                    else{
                        var column4_text = document.createTextNode("-");
                    }
                    column4.appendChild(column4_text);
                    row.appendChild(column1);
                    row.appendChild(column2);
                    row.appendChild(column3);
                    row.appendChild(column4);
                    tbody.appendChild(row);
                }
            }
        }
        else {
            $.each(lines, function (n, elem) {
                if (n!=resolved) {
                    var row = document.createElement('tr');
                    var column = document.createElement('td');
                    var cell_text = document.createTextNode(elem.split(':')[1].split('"')[1]);
                    column.appendChild(cell_text);
                    row.appendChild(column);
                    tbody.appendChild(row);
                }
            });
        }
    }
    table.appendChild(tbody);
    return table;
}

function downloadFile(){
    $.fileDownload('Results/capture.pcap').done(function () { });
}

$.get('Results/pcap_results',function(data){
    var lines = data.split("\n");
    var table=pcapResultsPresentation(lines);
    table.setAttribute("style", "overflow-x:hidden");
    table.setAttribute("id", "network_capture_table")
    var heading=document.createElement('h5');
    var heading_Text=document.createTextNode("Analysis of pcap_results");
    heading.appendChild(heading_Text);
    $('#network_traffic').append(heading);
    $('#network_traffic').append(table);
    var title = "Network Capture";
    pdf.setTextColor(0, 102, 204);
    pdf.setFont("helvetica", "normal");
    pdf.setFontSize(20);
    pdf.text(title, 20, pdf.autoTableEndPosY() + 45);
    var headers=[];
    var data=[];
    headers.push(" ");
    var table=document.getElementById("network_capture_table");
    for (var k = 1; k < table.rows.length; k++) {
        var tableRow = table.rows[k];
        var rowData = [];
        rowData.push(tableRow);
        data.push(rowData);
    }
    pdf.autoTable(headers, data, {
        startY: pdf.autoTableEndPosY() + 60,
        margin: {horizontal: 20},
        styles: {overflow: 'linebreak'},
        bodyStyles: {valign: 'top'},
        columnStyles: {email: {columnWidth: 'wrap'}}
    });
}).error(function(){console.log("pcapresults file does not Exist")});

function pcapResultsPresentation(lines){

    var resolved=lines.length-1;
    var table=document.createElement('table');
    var tbody=document.createElement('tbody');
    if (resolved==0){
        var row=document.createElement('tr');
        table.className="table";
        var column=document.createElement('td');
        column.className="warning";
        var column_text=document.createTextNode("No Results Found");
        column.appendChild(column_text);
        row.appendChild(column);
        tbody.appendChild(row);
    }
    else {
        table.className="table table-striped";
        $.each(lines, function (n, elem) {
            if (n!=resolved) {
                var row = document.createElement('tr');
                var column = document.createElement('td');
                var cell_text = document.createTextNode(elem);
                column.appendChild(cell_text);
                row.appendChild(column);
                tbody.appendChild(row);
            }
        });
    }
    table.appendChild(tbody);
    return table;
}


function ResponderPresentation(lines,file){
    var resolved=lines.length-1;
    var table=document.createElement('table');
    var tbody=document.createElement('tbody');
    if (resolved==0){
        var row=document.createElement('tr');
        table.className="table";
        var column=document.createElement('td');
        column.className="warning";
        var column_text=document.createTextNode("No Results Found");
        column.appendChild(column_text);
        row.appendChild(column);
        tbody.appendChild(row);
    }
    else {
        table.className = "table table-striped";
        var line_items = [];
        $.each(lines, function (n, elem) {
            if (n != resolved) {
                line_items.push(elem);
            }
        });
        if (line_items[0].indexOf("Clear-Text")>=0) {
            var table_h = document.createElement('thead');
            var t_row = document.createElement('tr');
            var ht1 = document.createElement('th');
            var ht2 = document.createElement('th');
            ht1.setAttribute("style", "text-align:center");
            ht2.setAttribute("style", "text-align:center");
            var ht1_text = document.createTextNode("Name");
            var ht2_text = document.createTextNode("Password");
            ht1.appendChild(ht1_text);
            ht2.appendChild(ht2_text);
            t_row.appendChild(ht1);
            t_row.appendChild(ht2);
            table_h.appendChild(t_row);
            table.appendChild(table_h);

            var accInfo=[];
            for (var i=0; i<line_items.length; i++){
                var passDomain=[];
                passDomain['user']=line_items[i].split(':')[0];
                passDomain['pass']=line_items[i].split(':')[1];
                accInfo.push(passDomain);
            }
            for (var i=0; i<line_items.length; i++){
                var row=document.createElement('tr');
                var c1=document.createElement('td');
                var c2=document.createElement('td');
                var c1_text=document.createTextNode(accInfo[i]['user']);
                var c2_text=document.createTextNode(accInfo[i]['pass']);
                c1.appendChild(c1_text);
                c2.appendChild(c2_text);
                row.appendChild(c1);
                row.appendChild(c2);
                tbody.append(row);
            }

        }
        else {
            var table_h = document.createElement('thead');
            var t_row = document.createElement('tr');
            var ht1 = document.createElement('th');
            var ht2 = document.createElement('th');
            var ht3 = document.createElement('th');
            ht1.setAttribute("style", "text-align:center");
            ht2.setAttribute("style", "text-align:center");
            var ht1_text = document.createTextNode("Name");
            var ht2_text = document.createTextNode("Domain");
            ht1.appendChild(ht1_text);
            ht2.appendChild(ht2_text);
            t_row.appendChild(ht1);
            t_row.appendChild(ht2);
            t_row.appendChild(ht3);
            table_h.appendChild(t_row);
            table.appendChild(table_h);

            var domains = [];
            for (var i = 0; i < line_items.length; i++) {
                var nameDomain = [];
                var name = line_items[i].split(':')[0];
                nameDomain['name'] = name;
                var domain = line_items[i].split('::')[1].split(':')[0];
                nameDomain['domain'] = domain;
                nameDomain['full'] = line_items[i];
                domains.push(nameDomain);
            }
            for (var i = 0; i < line_items.length; i++) {
                var row = document.createElement('tr');
                var row_copy = document.createElement('tr');
                var c1 = document.createElement('td');
                var c2 = document.createElement('td');
                var c3 = document.createElement('td');
                c1.setAttribute("style", "text-align:center");
                c2.setAttribute("style", "text-align:center");
                c3.setAttribute("style", "text-align:right");
                var link = document.createElement('a');
                var c1_text = document.createTextNode(domains[i]['name']);
                var c2_text = document.createTextNode(domains[i]['domain']);
                var span_t = document.createElement('span');
                span_t.className = "glyphicon glyphicon-menu-down";
                var row_ctext = document.createTextNode(domains[i]['full']);
                row_copy.setAttribute("id", file + i);
                var span_t2 = document.createElement('span');
                span_t2.setAttribute("style", "word-wrap:break-word;display:inline-block;");
                span_t2.className = "col-xs-1 col-sm-1 col-md-2";
                span_t2.appendChild(row_ctext);
                row_copy.appendChild(span_t2);
                row_copy.setAttribute("style", "display:none");
                link.appendChild(span_t);
                var fileID=file+i;
                link.setAttribute("onclick", "showContent('"+fileID+"')");
                c1.appendChild(c1_text);
                c2.appendChild(c2_text);
                c3.appendChild(link);
                row.appendChild(c1);
                row.appendChild(c2);
                row.appendChild(c3);
                tbody.appendChild(row);
                tbody.appendChild(row_copy);
            }
        }
    }
    table.appendChild(tbody);
    return table;
}


function showContent(record){
    var id=document.getElementById(record);
    if (id.getAttribute("style").indexOf("display:none")>=0){
        id.setAttribute("style","display:inherit");
    }
    else{
        id.setAttribute("style","display:none");
    }
}

function ResponderTabs(files){
    var div=document.createElement('div');
    div.setAttribute("id", "responder_c");
    var tabs=document.createElement('ul');
    tabs.setAttribute("role","tablist");
    tabs.setAttribute("id", "responder_tabs");
    tabs.className="nav nav-tabs nav-justified";
    tabs.setAttribute("style", "margin-top:20px");
    var panel_content=document.createElement('div');
    panel_content.className="tab-content";
    panel_content.setAttribute("style", "margin-top:20px");
    var file_headers=[];
    var headers=[];
    for (var i=0; i<files.length; i++){
        var file={};
        var h=files[i].substring(0,files[i].lastIndexOf('-'));
        file['header']=h;
        file['file']=files[i];
        headers.push(h);
        file_headers.push(file);
    }
    var unique_headers=[];
    for (var i=0; i<headers.length; i++){
        var vl=headers[i];
        var found=false;
        for (var k=i+1; k<headers.length; k++){
            if (vl.localeCompare(headers[k])>=0){
               found=true;
            }
        }
        if (found==false){
            unique_headers.push(vl);
        }
    }
    
    $.each(files, function(index, value){
        var file=value;
        var i=index;
        var path='Results/Responder_logs/logs/'+ file;
        $.get(path, function(data) {
            var lines = data.split("\n");
            var contentn = file + '_content';
            var tabPanel = createTabPanels(contentn, i);
            var responderi = file + '_responder';
            var list_i = newTabResponder(responderi, '#' + contentn, file, i);
            var table = ResponderPresentation(lines, file);
            table.setAttribute("id", file+"responder_table" + i);
            tabPanel.appendChild(table);
            panel_content.appendChild(tabPanel);
            tabs.appendChild(list_i);
            var retrieveContents=localStorage.getItem("pdf");
            var contents=JSON.parse(retrieveContents);
            contents.push(file+"responder_table"+i);
            localStorage.setItem("pdf",JSON.stringify(contents));
            });
    });

    div.appendChild(tabs);
    div.appendChild(panel_content);
    $('#responder_content').append(div);
}

function createTabPanels(id,counter){
    var panel=document.createElement('div');
    panel.setAttribute("role", "tabpanel");
    panel.setAttribute("id", id);
    if (counter==0){
        panel.className="tab-pane active";
    }
    else{
        panel.className="tab-pane";
    }
    return panel;
}

function newTabResponder(id,contentID,tabName,counter){
    var list_item=document.createElement('li');
    list_item.setAttribute("role", "presentation");
    var ref=document.createElement('a');
    ref.setAttribute("id",id);
    ref.setAttribute("href",contentID);
    ref.setAttribute("role", "tab");
    ref.setAttribute("data-toggle", "tab");
    ref.setAttribute("onclick", "changeResponderTab('"+contentID+"')");
    var t=tabName.substring(0, tabName.lastIndexOf('-'));
    var text=document.createTextNode(t);
    ref.appendChild(text);
    list_item.appendChild(ref);
    if (counter==0){
        list_item.className="active";
        var c=contentID.split("#")[1];
        localStorage.setItem("previousResponder", c);
    }
    return list_item;
}

function findResponderElements(){
    var dir='readDirectory.php';
    var directory="Results/Responder_logs/logs/";
    var arg={directory:directory};

    $.ajax({
        url:dir,
        type:'GET',
        dataType: 'json',
        success:function(data) {
            var response= data;
            var validFiles=[];
            for (var i=0; i<response.Files.length; i++) {
                if ((response.Files[i].indexOf(".log")>=0) || (response.Files[i].indexOf("mvp_names")>=0) || (response.Files[i].indexOf("model")>=0) || (response.Files[i].indexOf("nfs_hosts")>=0) || (response.Files[i].indexOf("nameservers")>=0) || (response.Files[i].indexOf("liveip_hosts")>=0) || (response.Files[i].indexOf("live_ips")>=0) || (response.Files[i].indexOf("web_hosts")>=0) || (response.Files[i].indexOf("running_status")>=0) || (response.Files[i].indexOf("mvps")>=0) || (response.Files[i].indexOf("win_hosts")>=0) || (response.Files[i].indexOf("..")>=0) || ((response.Files[i].length==1) && (response.Files[i].indexOf('.')>=0))){}
                else{
                    validFiles.push(response.Files[i])
                }
            }
           ResponderTabs(validFiles);
        },
        error:function(){
            console.log("Error");
        },
        data: arg
    });
}

function findResults(){
    localStorage.setItem("previous","network_traffic");
    var dir='readDirectory.php';
    var directory="Results/";
    var arg={directory:directory};
    $.ajax({
        url:dir,
        type:'GET',
        dataType: 'json',
        success:function(data) {
            var response= data;
            var validFiles=[];
            for (var i=0; i<response.Files.length; i++) {
                if ((response.Files[i].indexOf("statics")>=0) || (response.Files[i].indexOf("mvp_names")>=0) || (response.Files[i].indexOf("model")>=0) || (response.Files[i].indexOf("nfs_hosts")>=0) || (response.Files[i].indexOf("nameservers")>=0) || (response.Files[i].indexOf("liveip_hosts")>=0) || (response.Files[i].indexOf("live_ips")>=0) || (response.Files[i].indexOf("web_hosts")>=0) || (response.Files[i].indexOf("running_status")>=0) || (response.Files[i].indexOf("mvps")>=0) || (response.Files[i].indexOf("win_hosts")>=0) || (response.Files[i].indexOf("pcap_results")>=0)|| (response.Files[i].indexOf(".DS_Store")>=0)|| (response.Files[i].indexOf("capture.pcap")>=0)|| (response.Files[i].indexOf("avail_ips")>=0) || (response.Files[i].indexOf("..")>=0) || ((response.Files[i].length==1) && (response.Files[i].indexOf('.')>=0))){}
                else{
                    validFiles.push(response.Files[i])
                }
            }
            $.each(validFiles, function(index, value){
                var path=directory+value;
                if (value.localeCompare('Responder_logs')==0){
                    newTab("responder","#responder_content","Credentials Capture");
                    findResponderElements();
                }
                else {
                    $.get(path, function (data) {
                        var title = findTitle(value);
                        if (title.localeCompare("network_scanner")==0){
                            var scan=[];
                            scan['filename']=value;
                            scan['data']=lines;
                            newDropdownItem(scan);
                        }
                        else{
                            newTab(value, "#" + value + "_content", title);
                            var lines = data.split("\n");
                            Presentation(lines, value);
                        }
                    });
                }
            });
        },
        error:function(){
            console.log("Error");
        },
        data: arg
    });

}

function findTitle(filename){
    switch (filename){
        case 'avail_ips': return 'Available IPs';
            break;
        case 'hostnames': return 'Hostnames';
            break;
        case 'unique_CIDR': return 'CIDR Discovered';
            break;
        case 'unique_hosts': return 'Hosts Discovered';
            break;
        case 'unique_subnets': return 'Subnets Discovered';
            break;
        case 'hostnames' : return 'Hostnames';
            break;
        case 'used_ips': return 'Used IPs';
            break;
        case 'ips_discovered': return "IPs Discovered";
            break;
        case 'windows': return 'network_scanner';
            break;
        case 'ftp': return 'network_scanner';
            break;
        case 'mysql': return 'network_scanner';
            break;
        case 'webservers80': return 'network_scanner';
            break;
        case 'webservers443': return 'network_scanner';
            break;
        case 'webservers8080': return 'network_scanner';
            break;
        case 'webservers4443': return 'network_scanner';
            break;
        case 'webservers8081': return 'network_scanner';
            break;
        case 'webservers8181': return 'network_scanner';
            break;
        case 'webservers9090': return 'network_scanner';
            break;
        case 'mssql': return 'network_scanner';
            break;
        case 'oracle': return 'network_scanner';
            break;
        case 'nfs': return 'network_scanner';
            break;
        case 'webservers': return 'network_scanner';
            break;
        case 'webs': return 'Webservers';
            break;
        case 'printers': return 'network_scanner';
            break;
        case 'mongo': return 'network_scanner';
            break;
        case 'telnet': return 'network_scanner';
            break;
        case 'vnc': return 'network_scanner';
            break;
        case 'dns': return 'network_scanner';
            break;
        case 'phpmyadmin': return 'network_scanner';
            break;
        case 'tightvnc': return 'network_scanner';
            break;
        case 'websphere': return 'network_scanner';
            break;
        case 'firebird': return 'network_scanner';
            break;
        case 'xserver': return 'network_scanner';
            break;
        case 'svn': return 'network_scanner';
            break;
        case 'snmp': return 'network_scanner';
            break;
        case 'voip': return 'network_scanner';
            break;
        case 'rlogin': return 'network_scanner';
            break;
        case 'openvpn': return 'network_scanner';
            break;
        case 'ipsec': return 'network_scanner';
            break;
        case 'ldap': return 'network_scanner';
            break;
        case 'pop3': return 'network_scanner';
            break;
        case 'smtp': return 'network_scanner';
            break;
        case 'sap_mgmt': return 'network_scanner';
            break;
        case 'sap_router': return 'network_scanner';
            break;
        case 'sap_gui': return 'network_scanner';
            break;
        case 'sap_icf': return 'network_scanner';
            break;
        case 'java_rmi': return 'network_scanner';
            break;
        case 'isql': return 'network_scanner';
            break;
        case'clamav': return 'network_scanner';
            break;
        case 'finger': return 'network_scanner';
            break;
        case 'distcc': return 'network_scanner';
            break;
        case 'webmin': return 'network_scanner';
            break;
        case 'pjl': return 'network_scanner';
            break;
        case 'informix_serv': return 'network_scanner';
            break;
        case 'h323': return 'network_scanner';
            break;
        case 'vsphere': return 'network_scanner';
            break;
        case 'informix_db': return 'network_scanner';
            break;
        case 'imap': return 'network_scanner';
            break;
        case 'lotus_notes': return 'network_scanner';
            break;
        case'sql_resolution': return 'network_scanner';
            break;
        case 'upnp': return 'network_scanner';
            break;
        case 'radius': return 'network_scanner';
            break;
        case 'http_titles': return 'HTTP Titles';
            break;
        case 'shares': return 'Enumerated Shares';
            break;
        case 'smb_users': return 'SMB Users Enumeration';
            break;
        case 'nfs_enum': return 'NFS Enumeration';
            break;
        case 'wafed': return 'WAF Enum';
            break;
        case 'mysql_enum': return 'MYSQL Enumeration';
            break;
        case 'mssql_enum': return 'MSSQL Enum';
            break;
        case 'ftp_enum': return 'FTP Enumeration';
            break;
        case 'snmp_enum': return 'SNMP Enum';
            break;
        case 'wifis': return 'Wireless Networks';
            break;
        case 'blues': return 'Bluetooth Devices';
            break;
        case 'os_enum': return 'OS Enumeration';
            break;
        default: return filename;
    }
}

function Presentation(lines,filename){
    var table;
    var contents;
    switch (filename){
        case 'wifis': table=WifisPresentation(lines);
            table.setAttribute("id", "wifis_table");
            $("#"+filename+"_content").append(table);
            var retrieveContents=localStorage.getItem("pdf");
            contents=JSON.parse(retrieveContents);
            contents.push("wifis_table");
            localStorage.setItem("pdf",JSON.stringify(contents));
            break;
        case 'http_titles': table=http_title_presentation(lines);
            table.setAttribute("id", "http_titles_table");
            $("#"+filename+"_content").append(table);
            var retrieveContents=localStorage.getItem("pdf");
            contents=JSON.parse(retrieveContents);
            contents.push("http_titles_table");
            localStorage.setItem("pdf",JSON.stringify(contents));
            break;
        case 'smb_users': table=enum_presentation(lines,filename);
            table.setAttribute("id", "smb_users_table");
            $("#"+filename+"_content").append(table);
            var retrieveContents=localStorage.getItem("pdf");
            contents=JSON.parse(retrieveContents);
            contents.push("smb_users_table");
            localStorage.setItem("pdf",JSON.stringify(contents));
            break;
        case 'shares': table=enum_presentation(lines,filename);
            table.setAttribute("id", "shares_enum_table");
            $("#"+filename+"_content").append(table);
            var retrieveContents=localStorage.getItem("pdf");
            contents=JSON.parse(retrieveContents);
            contents.push("shares_enum_table");
            localStorage.setItem("pdf",JSON.stringify(contents));
            break;
        case 'nfs_enum': table=nfs_presentation(lines);
            table.setAttribute("id", "nfs_enum_table");
            $("#"+filename+"_content").append(table);
            var retrieveContents=localStorage.getItem("pdf");
            contents=JSON.parse(retrieveContents);
            contents.push("nfs_enum_table");
            localStorage.setItem("pdf",JSON.stringify(contents));
            break;
        case 'wafed': table=waf_presentation(lines);
            table.setAttribute("id", "wafed_enum_table");
            $("#"+filename+"_content").append(table);
            var retrieveContents=localStorage.getItem("pdf");
            contents=JSON.parse(retrieveContents);
            contents.push("wafed_enum_table");
            localStorage.setItem("pdf",JSON.stringify(contents));
            break;
        case 'mysql_enum': table=mysql_presentation(lines);
            table.setAttribute("id", "mysql_enum_table");
            $("#"+filename+"_content").append(table);
            var retrieveContents=localStorage.getItem("pdf");
            contents=JSON.parse(retrieveContents);
            contents.push("mysql_enum_table");
            localStorage.setItem("pdf",JSON.stringify(contents));
            break;
        case 'mssql_enum':table=mssql_presentation(lines);
            table.setAttribute("id", "mssql_enum_table");
            $("#"+filename+"_content").append(table);
            var retrieveContents=localStorage.getItem("pdf");
            contents=JSON.parse(retrieveContents);
            contents.push("mssql_enum_table");
            localStorage.setItem("pdf",JSON.stringify(contents));
            break;
        case 'ftp_enum': table=enum_presentation(lines,filename);
            table.setAttribute("id", "ftp_enum_table");
            $("#"+filename+"_content").append(table);
            var retrieveContents=localStorage.getItem("pdf");
            contents=JSON.parse(retrieveContents);
            contents.push("ftp_enum_table");
            localStorage.setItem("pdf",JSON.stringify(contents));
            break;
        case 'snmp_enum':table=snmp_presentation(lines);
            table.setAttribute("id", "snmp_enum_table");
            $("#"+filename+"_content").append(table);
            var retrieveContents=localStorage.getItem("pdf");
            contents=JSON.parse(retrieveContents);
            contents.push("snmp_enum_table");
            localStorage.setItem("pdf",JSON.stringify(contents));
            break;
      
        case 'blues': table=BluesPresentation(lines,filename);
            table.setAttribute("id", "blues_table");
            $("#"+filename+"_content").append(table);
            var retrieveContents=localStorage.getItem("pdf");
            contents=JSON.parse(retrieveContents);
            contents.push("blues_table");
            localStorage.setItem("pdf",JSON.stringify(contents));
            break;
        default: table=filePresentation(lines);
            table.setAttribute("id", filename+"_table");
            $("#"+filename+"_content").append(table);
            var retrieveContents=localStorage.getItem("pdf");
            contents=JSON.parse(retrieveContents);
            contents.push(filename+"_table");
            localStorage.setItem("pdf",JSON.stringify(contents));
            break;
    }
}


function createDropDown(){
    var dropdowntab=document.createElement('li');
    dropdowntab.className="dropdown";
    dropdowntab.setAttribute("role","presentation");
    dropdowntab.setAttribute("id", "dropdowntab_scanners");
    var dropdownA=document.createElement("a");
    dropdownA.className="dropdown-toggle";
    dropdownA.setAttribute("data-toggle", "dropdown");
    dropdownA.setAttribute("role","tab");
    dropdownA.setAttribute("aria-haspopup","true");
    dropdownA.setAttribute("aria-expanded","false");
    dropdownA.setAttribute("href","#");
    var ttext=document.createTextNode('Network Scanners');
    dropdownA.appendChild(ttext);
    var spant=document.createElement('span');
    spant.classname="caret";
    var dropdownmenu=document.createElement('ul');
    dropdownmenu.className="dropdown-menu";
    dropdownmenu.setAttribute("id", "dropdownmenu_scanners");
    dropdownA.appendChild(spant);
    dropdowntab.appendChild(dropdownA);
    dropdowntab.appendChild(dropdownmenu);
    $('#warBerry_tabs').append(dropdowntab);
}

function newDropdownItem(scan){
    var directory="Results/";
    var path=directory+scan['filename'];
    $.get(path, function (data) {
        var lines=data.split("\n");
        var table=filePresentation(lines);
        table.setAttribute("id", scan['filename']);
        table.setAttribute("style", "display:none");
        $('#hidden-elements').append(table);
        var retrieveContents=localStorage.getItem("pdf");
        contents=JSON.parse(retrieveContents);
        contents.push(scan['filename']);
        localStorage.setItem("pdf",JSON.stringify(contents));
    });
    var newItem=document.createElement('li');
    var t=findItemTitle(scan['filename']);
    var litext=document.createTextNode(t);
    var a=document.createElement('a');
    a.setAttribute('onclick',"show_scanner_content('"+scan['filename']+"')");
    a.appendChild(litext);
    newItem.appendChild(a);
    $('#dropdownmenu_scanners').append(newItem);
}

function findItemTitle(filename){
    switch (filename){
        case 'windows': return 'Windows';
            break;
        case 'ftp': return 'FTP';
            break;
        case 'mysql': return 'MySQL';
            break;
        case 'webservers80': return 'Web Servers 80';
            break;
        case 'webservers443': return 'Web Servers 443';
            break;
        case 'webservers8080': return 'Web Servers 8080';
            break;
        case 'webservers4443': return 'Web Servers 4443';
            break;
        case 'webservers8081': return 'Web Servers 8081';
            break;
        case 'webservers8181': return 'Web Servers 8181';
            break;
        case 'webservers9090': return 'Web Servers 9090';
            break;
        case 'mssql': return 'MSSQL';
            break;
        case 'oracle': return 'Oracle';
            break;
        case 'nfs': return 'NFS';
            break;
        case 'webservers': return 'Web Servers';
            break;
        case 'printers': return 'Printers';
            break;
        case 'mongo': return 'Mongo';
            break;
        case 'telnet': return 'Telnet';
            break;
        case 'vnc': return 'VNC';
            break;
        case 'dns': return 'DNS';
            break;
        case 'phpmyadmin': return 'PhpMyAdmin';
            break;
        case 'tightvnc': return 'Tight VNC';
            break;
        case 'websphere': return 'WebSphere';
            break;
        case 'firebird': return 'FireBird';
            break;
        case 'xserver': return 'XServer';
            break;
        case 'svn': return 'SVN';
            break;
        case 'snmp': return 'SNMP';
            break;
        case 'voip': return 'VOIP';
            break;
        case 'rlogin': return 'r Login';
            break;
        case 'openvpn': return 'Open VPN';
            break;
        case 'ipsec': return 'IP Sec';
            break;
        case 'ldap': return 'LDAP';
            break;
        case 'pop3': return 'POP3';
            break;
        case 'smtp': return 'SMTP';
            break;
        case 'sap_mgmt': return 'SAP MGMT';
            break;
        case 'sap_router': return 'SAP Router';
            break;
        case 'sap_gui': return 'SAP GUI';
            break;
        case 'sap_icf': return 'SAP ICF';
            break;
        case 'java_rmi': return 'JAVA RMI';
            break;
        case 'isql': return 'ISQL';
            break;
        case'clamav': return 'CLAMAV';
            break;
        case 'finger': return 'FINGER';
            break;
        case 'distcc': return 'DISTCC';
            break;
        case 'webmin': return 'Webmin';
            break;
        case 'pjl': return 'PJL';
            break;
        case 'informix_serv': return 'Informix Serv';
            break;
        case 'h323': return 'H323';
            break;
        case 'vsphere': return 'VSphere';
            break;
        case 'informix_db': return 'Informix DB';
            break;
        case 'imap': return 'IMAP';
            break;
        case 'lotus_notes': return 'Lotus Notes';
            break;
        case 'sql_resolution': return 'SQL Resolution Service';
            break;
        case 'upnp': return 'UPNP';
            break;
        case 'radius': return 'RADIUS';
            break;
    }

}

function findPDFTitle(filename){
    switch (filename){
        case 'avail_ips': return 'Available IPs';
            break;
        case 'hostnames_table': return 'Hostnames';
            break;
        case 'unique_CIDR_table': return 'CIDR';
            break;
        case 'unique_hosts_table': return 'Hosts';
            break;
        case 'unique_subnets_table': return 'Available Subnets';
            break;
        case 'hostnames' : return 'Hostnames';
            break;
        case 'used_ips_table': return 'Used IPs';
            break;
        case 'ips_discovered_table': return "IPs";
            break;
        case 'windows': return 'Windows';
            break;
        case 'ftp': return 'FTP';
            break;
        case 'mysql': return 'MySQL';
            break;
        case 'webs_table': return 'Webservers';
            break;
        case 'webservers80': return 'Web Servers 80';
            break;
        case 'webservers443': return 'Web Servers 443';
            break;
        case 'webservers8080': return 'Web Servers 8080';
            break;
        case 'webservers4443': return 'Web Servers 4443';
            break;
        case 'webservers8081': return 'Web Servers 8081';
            break;
        case 'webservers8181': return 'Web Servers 8181';
            break;
        case 'webservers9090': return 'Web Servers 9090';
            break;
        case 'mssql': return 'MSSQL';
            break;
        case 'oracle': return 'Oracle';
            break;
        case 'nfs': return 'NFS';
            break;
        case 'webservers': return 'Web Servers';
            break;
        case 'printers': return 'Printers';
            break;
        case 'mongo': return 'Mongo';
            break;
        case 'telnet': return 'Telnet';
            break;
        case 'vnc': return 'VNC';
            break;
        case 'dns': return 'DNS';
            break;
        case 'phpmyadmin': return 'PhpMyAdmin';
            break;
        case 'tightvnc': return 'Tight VNC';
            break;
        case 'websphere': return 'WebSphere';
            break;
        case 'firebird': return 'FireBird';
            break;
        case 'xserver': return 'XServer';
            break;
        case 'svn': return 'SVN';
            break;
        case 'snmp': return 'SNMP';
            break;
        case 'voip': return 'VOIP';
            break;
        case 'rlogin': return 'r Login';
            break;
        case 'openvpn': return 'Open VPN';
            break;
        case 'ipsec': return 'IP Sec';
            break;
        case 'ldap': return 'LDAP';
            break;
        case 'pop3': return 'POP3';
            break;
        case 'smtp': return 'SMTP';
            break;
        case 'http_titles_table': return 'HTTP Titles';
            break;
        case 'shares_enum_table': return 'Shares Enum';
            break;
        case 'smb_users_table': return 'SMB Users Enumeration';
            break;
        case 'nfs_enum_table': return 'NFS Enum';
            break;
        case 'wafed_enum_table': return 'WAF Enum';
            break;
        case 'mysql_enum_table': return 'MYSQL Enum';
            break;
        case 'mssql_enum_table': return 'MSSQL Enum';
            break;
        case 'ftp_enum_table': return 'FTP Enum';
            break;
        case 'snmp_enum_table': return 'SNMP Enum';
            break;
        case 'wifis_table': return 'Wireless Networks';
            break;
        case 'blues_table': return 'Bluetooth Devices';
            break;
        case 'sap_mgmt': return 'SAP MGMT';
            break;
        case 'sap_router': return 'SAP Router';
            break;
        case 'sap_gui': return 'SAP GUI';
            break;
        case 'sap_icf': return 'SAP ICF';
            break;
        case 'java_rmi': return 'JAVA RMI';
            break;
        case 'isql': return 'ISQL';
            break;
        case'clamav': return 'CLAMAV';
            break;
        case 'finger': return 'FINGER';
            break;
        case 'distcc': return 'DISTCC';
            break;
        case 'webmin': return 'Webmin';
            break;
        case 'pjl': return 'PJL';
            break;
        case 'informix_serv': return 'Informix Serv';
            break;
        case 'h323': return 'H323';
            break;
        case 'vsphere': return 'VSphere';
            break;
        case 'informix_db': return 'Informix DB';
            break;
        case 'imap': return 'IMAP';
            break;
        case 'lotus_notes': return 'Lotus Notes';
            break;
        case 'sql_resolution': return 'SQL Resolution Service';
            break;
        case 'upnp': return 'UPNP';
            break;
        case 'radius': return 'RADIUS';
            break;
        case 'os_enum': return 'OS Enumeration';
            break;
        default: return filename;
    }
}


function show_scanner_content(file){
    var directory="Results/";
    var path=directory+file;
    $.get(path, function (data) {
        var lines=data.split("\n");
        var table=filePresentation(lines);
        table.setAttribute("table", "shownTable");
        var net_scan=document.getElementById("network_scanner_content");
        net_scan.innerHTML="";
        $('#network_scanner_content').append(table);
        $('#dropdowntab_scanners').tab('show');
        var previous=localStorage.getItem("previous");
        var content=document.getElementById('network_scanner_content');
        content.style.display="inherit";
        document.getElementById(previous).setAttribute("style", "display:none");
    });
}

function BluesPresentation(lines){
    var resolved=lines.length-1;
    var table=document.createElement('table');
    var tbody=document.createElement('tbody');
    if (resolved==0){
        var row=document.createElement('tr');
        table.className="table";
        var column=document.createElement('td');
        column.className="warning";
        var column_text=document.createTextNode("No Results Found");
        column.appendChild(column_text);
        row.appendChild(column);
        tbody.appendChild(row);
    }
    else {
        var table_h = document.createElement('thead');
        var t_row = document.createElement('tr');
        var ht1 = document.createElement('th');
        var ht2 = document.createElement('th');
        var ht1_text = document.createTextNode("Device");
        var ht2_text = document.createTextNode("MAC Address");
        ht1.appendChild(ht1_text);
        ht2.appendChild(ht2_text);
        t_row.appendChild(ht1);
        t_row.appendChild(ht2);
        table_h.appendChild(t_row);
        table.appendChild(table_h);

        table.className = "table table-striped pre-scrollable";
        var line_items = [];
        $.each(lines, function (n, elem) {
            if (n!=resolved) {
                var c = elem.lastIndexOf(' ');
                var device_d = [];
                device_d["device_name"] = elem.substring(0, c);
                device_d['mac'] = elem.substring(c + 1);
                line_items.push(device_d);
            }
        });

        var device_n=[];
        var mac_n=[];

        for(var i = 0; i <line_items.length; i++) {
            if(!mac_n.includes(line_items[i]['mac'])) {
                device_n.push(line_items[i]['device_name']);
                mac_n.push(line_items[i]['mac']);
            }
        }
        for (var i=0; i<device_n.length; i++){
            var row = document.createElement('tr');
            var column1 = document.createElement('td');
            var column2 = document.createElement('td');
            var cell_text1 = document.createTextNode(device_n[i]);
            var cell_text2 = document.createTextNode(mac_n[i]);
            column1.appendChild(cell_text1);
            column2.appendChild(cell_text2);
            row.appendChild(column1);
            row.appendChild(column2);
            tbody.appendChild(row);
        }

    }
    table.appendChild(tbody);
    return table;
}


function createPDFile(){
    var delay=2000; //2 second
    setTimeout(function() {
        var convertTables=localStorage.getItem("pdf");
        var alltables=JSON.parse(convertTables);
        for (var i=0; i<alltables.length; i++) {
            var tableID = alltables[i];
            var headers = [];
            var data = [];
            var table = document.getElementById(tableID);
            if (tableID.lastIndexOf('responder') >= 0) {
                var t=tableID.substring(0,tableID.split("responder")[0].lastIndexOf('-'));
                var title = "Credentials Capture: "+ t;
                pdf.setTextColor(0, 102, 204);
                pdf.setFont("helvetica", "normal");
                pdf.setFontSize(20);
                pdf.text(title, 20, pdf.autoTableEndPosY() + 45);
                headers.push(table.rows[0].cells[0].innerHTML);
                headers.push(table.rows[0].cells[1].innerHTML);
                headers.push("Details");
                for (var k = 1; k < table.rows.length-1; k=k+2) {
                    var tableRow = table.rows[k];
                    var rowData = [];
                    for (var l = 0; l < 2; l++) {
                        rowData.push(tableRow.cells[l].innerHTML);
                    }
                    rowData.push(table.rows[k+1].innerHTML.split('>')[1].split('<')[0]);
                    data.push(rowData);
                }
            }
            else {
                var title = findPDFTitle(tableID);
                pdf.setTextColor(0, 102, 204);
                pdf.setFont("helvetica", "normal");
                pdf.setFontSize(20);
                pdf.text(title, 20, pdf.autoTableEndPosY() + 45);
                if (table.rows[0].cells[0].outerHTML.indexOf('th>') >= 0) {
                    for (var k = 0; k < table.rows[0].cells.length; k++) {
                        headers.push(table.rows[0].cells[k].innerHTML);
                    }
                    for (var k = 1; k < table.rows.length; k++) {
                        var tableRow = table.rows[k];
                        var rowData = [];
                        for (var l = 0; l < tableRow.cells.length; l++) {
                            rowData.push(tableRow.cells[l].innerHTML);
                        }
                        data.push(rowData);
                    }
                }
                else {
                    var length = table.rows[0].cells.length;
                    for (var k = 0; k < length; k++) {
                        headers.push(" ");
                    }
                    for (var k = 0; k < table.rows.length; k++) {
                        var tableRow = table.rows[k];
                        var rowData = [];
                        for (var l = 0; l < tableRow.cells.length; l++) {
                            rowData.push(tableRow.cells[l].innerHTML);
                        }
                        data.push(rowData);
                    }
                }
            }
            pdf.autoTable(headers, data, {
                startY: pdf.autoTableEndPosY() + 60,
                margin: {horizontal: 20},
                styles: {overflow: 'linebreak'},
                bodyStyles: {valign: 'top'},
                columnStyles: {email: {columnWidth: 'wrap'}},
            });
        }
    }, delay);
}


function downloadPDF(){
    pdf.save("WarBerryReporting");
}