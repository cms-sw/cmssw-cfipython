import FWCore.ParameterSet.Config as cms

def HLTHFAsymmetryFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTHFAsymmetryFilter',
    HFHitCollection = cms.InputTag('hltHfreco'),
    ECut_HF = cms.double(3),
    OS_Asym_max = cms.double(0.2),
    SS_Asym_min = cms.double(0.8),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
