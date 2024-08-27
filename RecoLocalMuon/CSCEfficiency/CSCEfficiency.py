import FWCore.ParameterSet.Config as cms

def CSCEfficiency(**kwargs):
  mod = cms.EDFilter('CSCEfficiency',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
