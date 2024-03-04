import FWCore.ParameterSet.Config as cms

def ComphepSingletopFilterPy8(**kwargs):
  mod = cms.EDFilter('ComphepSingletopFilterPy8',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
