import FWCore.ParameterSet.Config as cms

def CandPtrSelector(**kwargs):
  mod = cms.EDFilter('CandPtrSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
