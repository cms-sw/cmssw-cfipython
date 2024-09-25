import FWCore.ParameterSet.Config as cms

def CSCTightHaloFilter(*args, **kwargs):
  mod = cms.EDFilter('CSCTightHaloFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
