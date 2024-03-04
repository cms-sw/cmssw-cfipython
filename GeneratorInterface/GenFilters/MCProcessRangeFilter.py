import FWCore.ParameterSet.Config as cms

def MCProcessRangeFilter(**kwargs):
  mod = cms.EDFilter('MCProcessRangeFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
