import FWCore.ParameterSet.Config as cms

def BunchCrossingFilter(**kwargs):
  mod = cms.EDFilter('BunchCrossingFilter',
    bunches = cms.vuint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
