import FWCore.ParameterSet.Config as cms

def DTCalibMuonSelection(*args, **kwargs):
  mod = cms.EDFilter('DTCalibMuonSelection',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
