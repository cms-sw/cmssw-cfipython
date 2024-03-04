import FWCore.ParameterSet.Config as cms

def DTCalibMuonSelection(**kwargs):
  mod = cms.EDFilter('DTCalibMuonSelection',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
