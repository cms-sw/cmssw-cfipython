import FWCore.ParameterSet.Config as cms

def L1Filter(**kwargs):
  mod = cms.EDFilter('L1Filter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
