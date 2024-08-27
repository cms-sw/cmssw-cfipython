import FWCore.ParameterSet.Config as cms

def CSCTightHaloFilter(**kwargs):
  mod = cms.EDFilter('CSCTightHaloFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
