# Size of variable arrays:
sizeAlgebraic = 59
sizeStates = 9
sizeConstants = 77

from math import *
from numpy import *
from scipy.integrate import ode
import pylab


def createLegends():
	""" Creates the lists of legends

	Arguments:

	Returns:
	legend_states -- list[str], list of legends for states.
	legend_algebraic -- list[str], list of legends for algebraic.
	legend_voi -- list[str], list of legends for voi.
	legend_constants -- list[str], list of legends for constants.

	"""
	legend_states = [""] * sizeStates
	legend_rates = [""] * sizeStates
	legend_algebraic = [""] * sizeAlgebraic
	legend_voi = ""
	legend_constants = [""] * sizeConstants
	legend_voi = "time in component environment (msec)"
	legend_algebraic[0] = "I_stim in component stimulus_protocol (pA_per_pF)"
	legend_constants[0] = "stim_start in component stimulus_protocol (msec)"
	legend_constants[1] = "stim_duration in component stimulus_protocol (msec)"
	legend_constants[2] = "stim_current in component stimulus_protocol (pA_per_pF)"
	legend_algebraic[45] = "I_tot in component membrane (pA_per_pF)"
	legend_algebraic[27] = "I_Ca_tot in component Ca_currents (pA_per_pF)"
	legend_algebraic[43] = "I_NS_tot in component NS_currents (pA_per_pF)"
	legend_algebraic[38] = "I_K_tot in component K_currents (pA_per_pF)"
	legend_states[0] = "v in component membrane (mV)"
	legend_constants[3] = "Cm in component parameters (uF_per_cm2)"
	legend_algebraic[16] = "ina in component I_Na (pA_per_pF)"
	legend_algebraic[28] = "ib in component I_b (pA_per_pF)"
	legend_algebraic[39] = "icl in component I_Cl (pA_per_pF)"
	legend_constants[4] = "P4 in component membrane (nM_per_L)"
	legend_constants[5] = "E2 in component membrane (nM_per_L)"
	legend_constants[6] = "P4_max in component membrane (nM_per_L)"
	legend_constants[7] = "E2_max in component membrane (nM_per_L)"
	legend_constants[24] = "mod_E2 in component membrane (dimensionless)"
	legend_constants[25] = "mod_P4 in component membrane (dimensionless)"
	legend_algebraic[57] = "J_tot in component Ca_Concentrations (mM_per_msec)"
	legend_algebraic[44] = "J_Ca_mem in component Ca_Concentrations (mM_per_msec)"
	legend_states[1] = "cai in component Ca_Concentrations (mM)"
	legend_algebraic[54] = "jnaca in component J_NaCa (mM_per_msec)"
	legend_algebraic[55] = "jpmca in component J_PMCA (mM_per_msec)"
	legend_algebraic[42] = "insca in component I_NSCa (pA_per_pF)"
	legend_constants[65] = "buff in component parameters (dimensionless)"
	legend_constants[66] = "AV in component parameters (cm2_per_uL)"
	legend_constants[67] = "zca in component parameters (dimensionless)"
	legend_constants[69] = "frdy in component parameters (coulomb_per_mole)"
	legend_algebraic[47] = "jcamem_plot in component Ca_Concentrations (M_per_msec)"
	legend_algebraic[58] = "jpmca_plot in component Ca_Concentrations (M_per_msec)"
	legend_algebraic[56] = "jnaca_plot in component Ca_Concentrations (M_per_msec)"
	legend_constants[8] = "conversion in component Ca_Concentrations (mM_to_M)"
	legend_constants[55] = "ki in component parameters (mM)"
	legend_constants[56] = "nai in component parameters (mM)"
	legend_constants[59] = "cli in component parameters (mM)"
	legend_constants[60] = "ko in component parameters (mM)"
	legend_constants[26] = "cao in component parameters (mM)"
	legend_constants[61] = "nao in component parameters (mM)"
	legend_constants[63] = "clo in component parameters (mM)"
	legend_constants[27] = "mgo in component parameters (mM)"
	legend_constants[28] = "zna in component parameters (dimensionless)"
	legend_constants[29] = "zk in component parameters (dimensionless)"
	legend_constants[68] = "R in component parameters (joule_per_kelvin_per_kilomole)"
	legend_constants[70] = "temp in component parameters (kelvin)"
	legend_constants[9] = "gna in component parameters (nS_per_pF)"
	legend_constants[10] = "gcal in component parameters (nS_per_pF)"
	legend_constants[30] = "ecal in component parameters (mV)"
	legend_constants[31] = "kmca in component parameters (mM)"
	legend_constants[11] = "gcat in component parameters (nS_per_pF)"
	legend_constants[32] = "ecat in component parameters (mV)"
	legend_constants[12] = "gkca in component parameters (nS_per_pF)"
	legend_constants[13] = "gb in component parameters (nS_per_pF)"
	legend_constants[14] = "gkv43 in component parameters (nS_per_pF)"
	legend_constants[15] = "gbka in component parameters (dimensionless)"
	legend_constants[16] = "gbkab in component parameters (dimensionless)"
	legend_constants[17] = "gcl in component parameters (nS_per_pF)"
	legend_constants[18] = "gns in component parameters (nS_per_pF)"
	legend_constants[33] = "PnsK in component parameters (dimensionless)"
	legend_constants[34] = "PnsNa in component parameters (dimensionless)"
	legend_constants[35] = "PnsCa in component parameters (dimensionless)"
	legend_constants[36] = "PnsCs in component parameters (dimensionless)"
	legend_constants[37] = "gnsCa in component parameters (dimensionless)"
	legend_constants[38] = "gnsNa in component parameters (dimensionless)"
	legend_constants[39] = "gnsK in component parameters (dimensionless)"
	legend_constants[40] = "gnsCs in component parameters (dimensionless)"
	legend_constants[41] = "PK in component parameters (dimensionless)"
	legend_constants[42] = "PNa in component parameters (dimensionless)"
	legend_constants[43] = "Jpmca in component parameters (mM_per_msec)"
	legend_constants[44] = "Kmpmca in component parameters (mM)"
	legend_constants[45] = "npmca in component parameters (dimensionless)"
	legend_constants[71] = "Jnaca in component parameters (mM_per_msec)"
	legend_constants[46] = "Kmallo in component parameters (mM)"
	legend_constants[47] = "nallo in component parameters (dimensionless)"
	legend_constants[72] = "ksat in component parameters (dimensionless)"
	legend_constants[76] = "xgamma in component parameters (dimensionless)"
	legend_constants[48] = "Kmnai in component parameters (mM)"
	legend_constants[49] = "Kmcai in component parameters (mM)"
	legend_constants[50] = "Kmnao in component parameters (mM)"
	legend_constants[51] = "Kmcao in component parameters (mM)"
	legend_constants[52] = "Fmax in component parameters (uN)"
	legend_constants[53] = "FKm in component parameters (nM)"
	legend_constants[54] = "Fn in component parameters (dimensionless)"
	legend_algebraic[6] = "vFRT in component parameters (dimensionless)"
	legend_constants[73] = "ena in component parameters (mV)"
	legend_constants[74] = "ek in component parameters (mV)"
	legend_constants[75] = "ecl in component parameters (mV)"
	legend_algebraic[12] = "enscc in component parameters (mV)"
	legend_algebraic[1] = "wss in component Ca_dependent_Force (dimensionless)"
	legend_algebraic[7] = "wtc in component Ca_dependent_Force (msec)"
	legend_constants[19] = "conversion in component Ca_dependent_Force (nM_to_mM)"
	legend_algebraic[2] = "Force in component Ca_dependent_Force (uN)"
	legend_states[2] = "w in component Ca_dependent_Force (dimensionless)"
	legend_algebraic[14] = "mss in component I_Na (dimensionless)"
	legend_algebraic[3] = "hss in component I_Na (dimensionless)"
	legend_algebraic[8] = "htc in component I_Na (msec)"
	legend_states[3] = "h in component I_Na (dimensionless)"
	legend_algebraic[22] = "ical in component I_CaL (pA_per_pF)"
	legend_algebraic[26] = "icat in component I_CaT (pA_per_pF)"
	legend_algebraic[20] = "dss in component I_CaL (dimensionless)"
	legend_algebraic[21] = "fss in component I_CaL (dimensionless)"
	legend_algebraic[18] = "fca in component I_CaL (dimensionless)"
	legend_algebraic[23] = "f2tc in component I_CaL (msec)"
	legend_states[4] = "f2 in component I_CaL (dimensionless)"
	legend_algebraic[24] = "bss in component I_CaT (dimensionless)"
	legend_algebraic[25] = "gss in component I_CaT (dimensionless)"
	legend_algebraic[37] = "iBKab in component I_BKab (pA_per_pF)"
	legend_algebraic[33] = "iBKa in component I_BKa (pA_per_pF)"
	legend_algebraic[29] = "ikv43 in component I_Kv43 (pA_per_pF)"
	legend_algebraic[4] = "qss in component I_Kv43 (dimensionless)"
	legend_algebraic[5] = "rss in component I_Kv43 (dimensionless)"
	legend_algebraic[9] = "qtc in component I_Kv43 (msec)"
	legend_algebraic[10] = "r1tc in component I_Kv43 (msec)"
	legend_algebraic[11] = "r2tc in component I_Kv43 (msec)"
	legend_states[5] = "q in component I_Kv43 (dimensionless)"
	legend_states[6] = "r1 in component I_Kv43 (dimensionless)"
	legend_states[7] = "r2 in component I_Kv43 (dimensionless)"
	legend_algebraic[30] = "xass_z in component I_BKa (dimensionless)"
	legend_algebraic[31] = "xass_vh in component I_BKa (mV)"
	legend_constants[20] = "conversion in component I_BKa (mM_to_M)"
	legend_algebraic[32] = "xass in component I_BKa (dimensionless)"
	legend_algebraic[34] = "xabss_z in component I_BKab (dimensionless)"
	legend_algebraic[35] = "xabss_vh in component I_BKab (mV)"
	legend_constants[21] = "conversion in component I_BKab (mM_to_M)"
	legend_algebraic[36] = "xabss in component I_BKab (dimensionless)"
	legend_algebraic[17] = "css in component I_Cl (dimensionless)"
	legend_algebraic[19] = "ctc in component I_Cl (msec)"
	legend_algebraic[13] = "K1cl in component I_Cl (mM)"
	legend_algebraic[15] = "K2cl in component I_Cl (dimensionless)"
	legend_states[8] = "c in component I_Cl (dimensionless)"
	legend_constants[57] = "fmg in component NS_currents (dimensionless)"
	legend_constants[22] = "tinyamount in component NS_currents (mM)"
	legend_algebraic[40] = "insna in component I_NSNa (pA_per_pF)"
	legend_algebraic[41] = "insk in component I_NSK (pA_per_pF)"
	legend_constants[64] = "gs_nao in component I_NSNa (dimensionless)"
	legend_constants[62] = "gs_ko in component I_NSK (dimensionless)"
	legend_constants[58] = "gs_cao in component I_NSCa (dimensionless)"
	legend_algebraic[46] = "f1naca in component J_NaCa (dimensionless)"
	legend_algebraic[48] = "f2naca in component J_NaCa (dimensionless)"
	legend_algebraic[49] = "fallo in component J_NaCa (dimensionless)"
	legend_algebraic[50] = "naca_Eup in component J_NaCa (mM4)"
	legend_algebraic[51] = "naca_Ed1 in component J_NaCa (dimensionless)"
	legend_algebraic[52] = "naca_Ed2 in component J_NaCa (mM4)"
	legend_algebraic[53] = "naca_Ed3 in component J_NaCa (mM4)"
	legend_constants[23] = "jnaca_sign in component J_NaCa (dimensionless)"
	legend_rates[0] = "d/dt v in component membrane (mV)"
	legend_rates[1] = "d/dt cai in component Ca_Concentrations (mM)"
	legend_rates[2] = "d/dt w in component Ca_dependent_Force (dimensionless)"
	legend_rates[3] = "d/dt h in component I_Na (dimensionless)"
	legend_rates[4] = "d/dt f2 in component I_CaL (dimensionless)"
	legend_rates[5] = "d/dt q in component I_Kv43 (dimensionless)"
	legend_rates[6] = "d/dt r1 in component I_Kv43 (dimensionless)"
	legend_rates[7] = "d/dt r2 in component I_Kv43 (dimensionless)"
	legend_rates[8] = "d/dt c in component I_Cl (dimensionless)"
	return (legend_states, legend_algebraic, legend_voi, legend_constants)


def initConsts():
	""" Initialises the constants

	Arguments:

	Return:
	states -- list[float], list of states.
	constants -- list[int], list of constants.

	"""
	constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
	constants[0] = 2000
	constants[1] = 4000
	constants[2] = -0.5
	states[0] = -53.90915441282156
	constants[3] = 1.0
	constants[4] = 14
	constants[5] = 45
	constants[6] = 53
	constants[7] = 140
	states[1] = 0.0001161881607214449
	constants[8] = 1000
	constants[9] = 0.0625
	constants[10] = 0.4
	constants[11] = 0.058
	constants[12] = 2.4
	constants[13] = 0.004
	constants[14] = 2.212
	constants[15] = 0.2
	constants[16] = 0.1
	constants[17] = 0.1875
	constants[18] = 0.0123
	constants[19] = 1e-6
	states[2] = 0.2345238135343783
	states[3] = 0.404599170710196
	states[4] = 0.9065967263076083
	states[5] = 0.2060363247740295
	states[6] = 0.1922244113609531
	states[7] = 0.1932803618375963
	constants[20] = 1000.0
	constants[21] = 1000.0
	states[8] = 0.0003764413740731269
	constants[22] = 1e-8
	constants[23] = -1
	constants[24] = constants[5]/constants[7]
	constants[25] = constants[4]/constants[6]
	constants[26] = 2.50000
	constants[27] = 0.500000
	constants[28] = 1.00000
	constants[29] = 1.00000
	constants[30] = 45.0000
	constants[31] = 0.00100000
	constants[32] = 42.0000
	constants[33] = 1.30000
	constants[34] = 0.900000
	constants[35] = 0.890000
	constants[36] = 1.00000
	constants[37] = 0.500000
	constants[38] = 1.00000
	constants[39] = 1.19000
	constants[40] = 1.60000
	constants[41] = 1.00000
	constants[42] = 0.350000
	constants[43] = 3.50000e-07
	constants[44] = 0.000500000
	constants[45] = 2.00000
	constants[46] = 0.000300000
	constants[47] = 4.00000
	constants[48] = 30.0000
	constants[49] = 0.00700000
	constants[50] = 87.5000
	constants[51] = 1.30000
	constants[52] = 3.00000
	constants[53] = 161.301
	constants[54] = 3.60205
	constants[55] = 140.000
	constants[56] = 4.00000
	constants[57] = 0.108043+0.903902/(1.00000+power(constants[27]/0.281007, 1.29834))
	constants[58] = ((1.00000/0.000525000)*0.0300000)/(1.00000+power(150.000/(constants[26]+constants[22]), 2.00000))
	constants[59] = 46.0000
	constants[60] = 6.00000
	constants[61] = 130.000
	constants[62] = ((1.00000/0.0123000)*0.0300000)/(1.00000+power(150.000/(constants[60]+constants[22]), 2.00000))
	constants[63] = 130.000
	constants[64] = ((1.00000/0.0123000)*0.0300000)/(1.00000+power(150.000/(constants[61]+constants[22]), 2.00000))
	constants[65] = 0.0169000
	constants[66] = 4.00000
	constants[67] = 2.00000
	constants[68] = 8314.00
	constants[69] = 96485.0
	constants[70] = 308.000
	constants[71] = 3.50000e-06
	constants[72] = 0.270000
	constants[73] = ((constants[68]*constants[70])/constants[69])*log(constants[61]/constants[56])
	constants[74] = ((constants[68]*constants[70])/constants[69])*log(constants[60]/constants[55])
	constants[75] = ((constants[68]*constants[70])/constants[69])*log(constants[59]/constants[63])
	constants[76] = 0.350000
	return (states, constants)


def computeRates(voi, states, constants):
	""" Computes rates of the system

	Arguments:
	voi -- list[flaot], list of voi.
	states -- list[float], list of states.
	constants -- list[int], list of constant values.

	Return:
	rates -- list[float], list of computed rates.

	"""
	rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
	algebraic[1] = 1.00000/(1.00000+power((constants[53]*constants[19])/states[1], constants[54]))
	algebraic[7] = 4000.00*(0.234845+(1.00000-0.234845)/(1.00000+power(states[1]/(constants[53]*constants[19]), constants[54])))
	rates[2] = (algebraic[1]-states[2])/algebraic[7]
	algebraic[3] = 1.00000/(1.00000+exp((states[0]+57.0000)/8.00000))
	algebraic[8] = 0.900000+1002.85/(1.00000+power((states[0]+47.5000)/1.50000, 2.00000))
	rates[3] = (algebraic[3]-states[3])/algebraic[8]
	algebraic[4] = 0.978613/(1.00000+exp(-(states[0]+18.6736)/26.6606))
	algebraic[9] = 500.000/(1.00000+power((states[0]+60.7100)/15.7900, 2.00000))
	rates[5] = (algebraic[4]-states[5])/algebraic[9]
	algebraic[5] = 1.00000/(1.00000+exp((states[0]+63.0000)/6.30000))
	algebraic[10] = 5000.00/(1.00000+power((states[0]+62.7133)/35.8611, 2.00000))
	rates[6] = (algebraic[5]-states[6])/algebraic[10]
	algebraic[11] = 30000.0+220000./(1.00000+exp((states[0]+22.0000)/4.00000))
	rates[7] = (algebraic[5]-states[7])/algebraic[11]
	algebraic[6] = (states[0]*constants[69])/(constants[68]*constants[70])
	algebraic[13] = 0.000600000*exp(2.53000*algebraic[6])
	algebraic[15] = 0.100000*exp(-5.00000*algebraic[6])
	algebraic[17] = 1.00000/(1.00000+algebraic[15]*(power(algebraic[13]/states[1], 2.00000)+algebraic[13]/states[1]+1.00000))
	algebraic[19] = -160.000+210.000/(1.00000+exp((states[0]+4.56000)/11.6200))+170.000/(1.00000+exp(-(states[0]+25.5000)/11.6200))
	rates[8] = (algebraic[17]-states[8])/algebraic[19]
	algebraic[21] = 1.00000/(1.00000+exp((states[0]+38.0000)/7.00000))
	algebraic[23] = 90.9699*(1.00000-1.00000/((1.00000+exp((states[0]+13.9629)/45.3782))*(1.00000+exp(-(states[0]+9.49866)/3.39450))))
	rates[4] = (algebraic[21]-states[4])/algebraic[23]
	algebraic[0] = customPiecewise([greater(voi , constants[0]) & less(voi , constants[0]+constants[1]), constants[2] , True, 0.00000])
	algebraic[20] = 1.00000/(1.00000+exp(-(states[0]+22.0000)/7.00000))
	algebraic[18] = 1.00000/(1.00000+power(states[1]/constants[31], 4.00000))
	algebraic[22] = ((constants[25]*constants[10])/constants[24])*algebraic[18]*algebraic[20]*algebraic[20]*(0.800000*algebraic[21]+0.200000*states[4])*(states[0]-constants[30])
	algebraic[24] = 1.00000/(1.00000+exp(-(states[0]+54.2300)/9.88000))
	algebraic[25] = 0.0200000+0.980000/(1.00000+exp((states[0]+72.9780)/4.64000))
	algebraic[26] = constants[11]*algebraic[24]*algebraic[24]*algebraic[25]*(states[0]-constants[32])
	algebraic[27] = algebraic[22]+algebraic[26]
	algebraic[12] = ((constants[68]*constants[70])/constants[69])*log((constants[33]*constants[60]+constants[34]*constants[61]+(4.00000*constants[35]*constants[26])/(1.00000+exp(algebraic[6])))/(constants[33]*constants[55]+constants[34]*constants[56]+(4.00000*constants[35]*states[1])/(1.00000+exp(algebraic[6]))))
	algebraic[42] = constants[57]*constants[58]*constants[37]*constants[18]*(states[0]-algebraic[12])
	algebraic[40] = constants[57]*constants[64]*constants[38]*constants[18]*(states[0]-algebraic[12])
	algebraic[41] = constants[57]*constants[62]*constants[39]*constants[18]*(states[0]-algebraic[12])
	algebraic[43] = algebraic[42]+algebraic[41]+algebraic[40]
	algebraic[34] = -0.681249/(1.00000+power((states[1]*constants[21]-0.218988)/0.428335, 2.00000))+1.40001/(1.00000+power((states[1]*constants[21]+228.710)/684.946, 2.00000))
	algebraic[35] = 8540.23/(1.00000+power((states[1]*constants[21]+0.401189)/0.00399115, 0.668054))-109.275
	algebraic[36] = 1.00000/(1.00000+exp((-algebraic[34]*constants[69]*(states[0]-algebraic[35]))/(constants[68]*constants[70])))
	algebraic[37] = constants[24]*constants[12]*constants[16]*algebraic[36]*(states[0]-constants[74])
	algebraic[30] = -0.749234/(1.00000+power((states[1]*constants[20]-0.0630535)/0.161942, 2.00000))+8.38384/(1.00000+power((states[1]*constants[20]+1538.29)/739.057, 2.00000))
	algebraic[31] = 5011.47/(1.00000+power((states[1]*constants[20]+0.237503)/0.000239278, 0.422910))-37.5137
	algebraic[32] = 1.00000/(1.00000+exp((-algebraic[30]*constants[69]*(states[0]-algebraic[31]))/(constants[68]*constants[70])))
	algebraic[33] = constants[24]*constants[12]*constants[15]*algebraic[32]*(states[0]-constants[74])
	algebraic[29] = constants[24]*constants[14]*states[5]*states[5]*(0.380000*states[6]+0.630000*states[7])*(states[0]-constants[74])
	algebraic[38] = algebraic[37]+algebraic[33]+algebraic[29]
	algebraic[14] = 1.00000/(1.00000+exp(-(states[0]+35.9584)/9.24013))
	algebraic[16] = ((constants[24]*constants[9])/constants[25])*algebraic[14]*algebraic[14]*algebraic[14]*states[3]*(states[0]-constants[73])
	algebraic[28] = constants[13]*(states[0]-constants[74])
	algebraic[39] = constants[17]*states[8]*(states[0]-constants[75])
	algebraic[45] = algebraic[16]+algebraic[39]+algebraic[28]+algebraic[27]+algebraic[43]+algebraic[38]
	rates[0] = -(algebraic[45]+algebraic[0])
	algebraic[44] = ((constants[66]*constants[3]*constants[65])/(constants[67]*constants[69]))*(algebraic[27]+algebraic[42])
	algebraic[49] = 1.00000/(1.00000+power(constants[46]/states[1], constants[47]))
	algebraic[46] = exp((constants[76]-1.00000)*algebraic[6])
	algebraic[48] = exp(constants[76]*algebraic[6])
	algebraic[50] = (power(constants[56], 3.00000))*constants[26]*algebraic[48]-(power(constants[61], 3.00000))*states[1]*algebraic[46]
	algebraic[51] = 1.00000+constants[72]*algebraic[46]
	algebraic[52] = constants[51]*(power(constants[56], 3.00000))+(power(constants[50], 3.00000))*states[1]+(power(constants[48], 3.00000))*constants[26]*(1.00000+states[1]/constants[49])
	algebraic[53] = constants[26]*(power(constants[56], 3.00000))+(power(constants[61], 3.00000))*states[1]+(power(constants[61], 3.00000))*constants[49]*(1.00000+power(constants[56]/constants[48], 3.00000))
	algebraic[54] = (constants[23]*constants[71]*algebraic[49]*algebraic[50])/(algebraic[51]*(algebraic[52]+algebraic[53]))
	algebraic[55] = constants[43]/(1.00000+power(constants[44]/states[1], constants[45]))
	algebraic[57] = algebraic[44]+algebraic[54]+algebraic[55]
	rates[1] = -algebraic[57]
	return(rates)


def computeAlgebraic(constants, states, voi):
	""" Computes algebraics of the system

	Arguments:
	constants -- list[int], list of constant values.
	states -- list[float], list of states.
	voi -- list[float], list of voi.

	Return:
	algebraic -- np.array[float], list of computed algebraics.

	"""
	algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
	states = array(states)
	voi = array(voi)
	algebraic[1] = 1.00000/(1.00000+power((constants[53]*constants[19])/states[1], constants[54]))
	algebraic[7] = 4000.00*(0.234845+(1.00000-0.234845)/(1.00000+power(states[1]/(constants[53]*constants[19]), constants[54])))
	algebraic[3] = 1.00000/(1.00000+exp((states[0]+57.0000)/8.00000))
	algebraic[8] = 0.900000+1002.85/(1.00000+power((states[0]+47.5000)/1.50000, 2.00000))
	algebraic[4] = 0.978613/(1.00000+exp(-(states[0]+18.6736)/26.6606))
	algebraic[9] = 500.000/(1.00000+power((states[0]+60.7100)/15.7900, 2.00000))
	algebraic[5] = 1.00000/(1.00000+exp((states[0]+63.0000)/6.30000))
	algebraic[10] = 5000.00/(1.00000+power((states[0]+62.7133)/35.8611, 2.00000))
	algebraic[11] = 30000.0+220000./(1.00000+exp((states[0]+22.0000)/4.00000))
	algebraic[6] = (states[0]*constants[69])/(constants[68]*constants[70])
	algebraic[13] = 0.000600000*exp(2.53000*algebraic[6])
	algebraic[15] = 0.100000*exp(-5.00000*algebraic[6])
	algebraic[17] = 1.00000/(1.00000+algebraic[15]*(power(algebraic[13]/states[1], 2.00000)+algebraic[13]/states[1]+1.00000))
	algebraic[19] = -160.000+210.000/(1.00000+exp((states[0]+4.56000)/11.6200))+170.000/(1.00000+exp(-(states[0]+25.5000)/11.6200))
	algebraic[21] = 1.00000/(1.00000+exp((states[0]+38.0000)/7.00000))
	algebraic[23] = 90.9699*(1.00000-1.00000/((1.00000+exp((states[0]+13.9629)/45.3782))*(1.00000+exp(-(states[0]+9.49866)/3.39450))))
	algebraic[0] = customPiecewise([greater(voi , constants[0]) & less(voi , constants[0]+constants[1]), constants[2] , True, 0.00000])
	algebraic[20] = 1.00000/(1.00000+exp(-(states[0]+22.0000)/7.00000))
	algebraic[18] = 1.00000/(1.00000+power(states[1]/constants[31], 4.00000))
	algebraic[22] = ((constants[25]*constants[10])/constants[24])*algebraic[18]*algebraic[20]*algebraic[20]*(0.800000*algebraic[21]+0.200000*states[4])*(states[0]-constants[30])
	algebraic[24] = 1.00000/(1.00000+exp(-(states[0]+54.2300)/9.88000))
	algebraic[25] = 0.0200000+0.980000/(1.00000+exp((states[0]+72.9780)/4.64000))
	algebraic[26] = constants[11]*algebraic[24]*algebraic[24]*algebraic[25]*(states[0]-constants[32])
	algebraic[27] = algebraic[22]+algebraic[26]
	algebraic[12] = ((constants[68]*constants[70])/constants[69])*log((constants[33]*constants[60]+constants[34]*constants[61]+(4.00000*constants[35]*constants[26])/(1.00000+exp(algebraic[6])))/(constants[33]*constants[55]+constants[34]*constants[56]+(4.00000*constants[35]*states[1])/(1.00000+exp(algebraic[6]))))
	algebraic[42] = constants[57]*constants[58]*constants[37]*constants[18]*(states[0]-algebraic[12])
	algebraic[40] = constants[57]*constants[64]*constants[38]*constants[18]*(states[0]-algebraic[12])
	algebraic[41] = constants[57]*constants[62]*constants[39]*constants[18]*(states[0]-algebraic[12])
	algebraic[43] = algebraic[42]+algebraic[41]+algebraic[40]
	algebraic[34] = -0.681249/(1.00000+power((states[1]*constants[21]-0.218988)/0.428335, 2.00000))+1.40001/(1.00000+power((states[1]*constants[21]+228.710)/684.946, 2.00000))
	algebraic[35] = 8540.23/(1.00000+power((states[1]*constants[21]+0.401189)/0.00399115, 0.668054))-109.275
	algebraic[36] = 1.00000/(1.00000+exp((-algebraic[34]*constants[69]*(states[0]-algebraic[35]))/(constants[68]*constants[70])))
	algebraic[37] = constants[24]*constants[12]*constants[16]*algebraic[36]*(states[0]-constants[74])
	algebraic[30] = -0.749234/(1.00000+power((states[1]*constants[20]-0.0630535)/0.161942, 2.00000))+8.38384/(1.00000+power((states[1]*constants[20]+1538.29)/739.057, 2.00000))
	algebraic[31] = 5011.47/(1.00000+power((states[1]*constants[20]+0.237503)/0.000239278, 0.422910))-37.5137
	algebraic[32] = 1.00000/(1.00000+exp((-algebraic[30]*constants[69]*(states[0]-algebraic[31]))/(constants[68]*constants[70])))
	algebraic[33] = constants[24]*constants[12]*constants[15]*algebraic[32]*(states[0]-constants[74])
	algebraic[29] = constants[24]*constants[14]*states[5]*states[5]*(0.380000*states[6]+0.630000*states[7])*(states[0]-constants[74])
	algebraic[38] = algebraic[37]+algebraic[33]+algebraic[29]
	algebraic[14] = 1.00000/(1.00000+exp(-(states[0]+35.9584)/9.24013))
	algebraic[16] = ((constants[24]*constants[9])/constants[25])*algebraic[14]*algebraic[14]*algebraic[14]*states[3]*(states[0]-constants[73])
	algebraic[28] = constants[13]*(states[0]-constants[74])
	algebraic[39] = constants[17]*states[8]*(states[0]-constants[75])
	algebraic[45] = algebraic[16]+algebraic[39]+algebraic[28]+algebraic[27]+algebraic[43]+algebraic[38]
	algebraic[44] = ((constants[66]*constants[3]*constants[65])/(constants[67]*constants[69]))*(algebraic[27]+algebraic[42])
	algebraic[49] = 1.00000/(1.00000+power(constants[46]/states[1], constants[47]))
	algebraic[46] = exp((constants[76]-1.00000)*algebraic[6])
	algebraic[48] = exp(constants[76]*algebraic[6])
	algebraic[50] = (power(constants[56], 3.00000))*constants[26]*algebraic[48]-(power(constants[61], 3.00000))*states[1]*algebraic[46]
	algebraic[51] = 1.00000+constants[72]*algebraic[46]
	algebraic[52] = constants[51]*(power(constants[56], 3.00000))+(power(constants[50], 3.00000))*states[1]+(power(constants[48], 3.00000))*constants[26]*(1.00000+states[1]/constants[49])
	algebraic[53] = constants[26]*(power(constants[56], 3.00000))+(power(constants[61], 3.00000))*states[1]+(power(constants[61], 3.00000))*constants[49]*(1.00000+power(constants[56]/constants[48], 3.00000))
	algebraic[54] = (constants[23]*constants[71]*algebraic[49]*algebraic[50])/(algebraic[51]*(algebraic[52]+algebraic[53]))
	algebraic[55] = constants[43]/(1.00000+power(constants[44]/states[1], constants[45]))
	algebraic[57] = algebraic[44]+algebraic[54]+algebraic[55]
	algebraic[2] = constants[52]*(states[2]-0.234500)
	algebraic[47] = algebraic[44]*constants[8]
	algebraic[56] = algebraic[54]*constants[8]
	algebraic[58] = algebraic[55]*constants[8]
	return algebraic


def customPiecewise(cases):
	""" Compute result of a piecewise function

	Arguments:
	cases -- list, list of piece cases.

	Return:
	
	"""
	return select(cases[0::2],cases[1::2])


def solveModel(init_states, constants):
	""" Solve model with ODE solver

	Arguments:
	init_states -- list[float], list of initial states.
	constants -- list[int], list of constant values.

	Return:

	"""
	# Set timespan to solve over
	voi = linspace(0, 10000, 100000)

	# Construct ODE object to solve
	r = ode(computeRates)
	r.set_integrator('vode', method='bdf', atol=1e-07, rtol=1e-07, max_step=0.1)
	r.set_initial_value(init_states, voi[0])
	r.set_f_params(constants)

	# Solve model
	states = array([[0.0] * len(voi)] * sizeStates)
	states[:,0] = init_states
	for (i,t) in enumerate(voi[1:]):
		if r.successful():
			r.integrate(t)
			states[:,i+1] = r.y
		else:
			break

	# Compute algebraic variables
	algebraic = computeAlgebraic(constants, states, voi)
	return (voi, states, algebraic)
