import FWCore.ParameterSet.Config as cms

def HcalMLTask(**kwargs):
  mod = cms.EDProducer('HcalMLTask',
    name = cms.untracked.string('HcalMLTask'),
    onnx_model_path_HB = cms.untracked.string('DQM/HcalTasks/data/HB_2022/CGAE_MultiDim_SPATIAL_vONNX_RCLv22_PIXEL_BT_BN_RIN_IPHI_MED_5218_v06_02_2023_21h01_stateful.onnx'),
    onnx_model_path_HE = cms.untracked.string('DQM/HcalTasks/data/HE_2022/CGAE_MultiDim_SPATIAL_vONNX_RCLv22_PIXEL_BT_BN_RIN_IPHI_MED_7763_v06_02_2023_22h55_stateful.onnx'),
    flagDecisionThr = cms.untracked.double(20),
    debug = cms.untracked.int32(0),
    runkeyVal = cms.untracked.int32(0),
    runkeyName = cms.untracked.string('pp_run'),
    ptype = cms.untracked.int32(1),
    mtype = cms.untracked.bool(True),
    subsystem = cms.untracked.string('Hcal'),
    tagHBHE = cms.untracked.InputTag('hcalDigis'),
    tagHO = cms.untracked.InputTag('hcalDigis'),
    tagHF = cms.untracked.InputTag('hcalDigis'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
