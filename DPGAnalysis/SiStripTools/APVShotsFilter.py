import FWCore.ParameterSet.Config as cms

def APVShotsFilter(**kwargs):
  mod = cms.EDFilter('APVShotsFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
