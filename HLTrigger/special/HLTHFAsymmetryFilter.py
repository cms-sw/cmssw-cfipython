import FWCore.ParameterSet.Config as cms

def HLTHFAsymmetryFilter(**kwargs):
  mod = cms.EDFilter('HLTHFAsymmetryFilter',
    HFHitCollection = cms.InputTag('hltHfreco'),
    ECut_HF = cms.double(3),
    OS_Asym_max = cms.double(0.2),
    SS_Asym_min = cms.double(0.8),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
