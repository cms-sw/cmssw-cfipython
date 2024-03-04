import FWCore.ParameterSet.Config as cms

def PFDQMEventSelector(**kwargs):
  mod = cms.EDFilter('PFDQMEventSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
