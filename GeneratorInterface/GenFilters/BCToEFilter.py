import FWCore.ParameterSet.Config as cms

def BCToEFilter(**kwargs):
  mod = cms.EDFilter('BCToEFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
