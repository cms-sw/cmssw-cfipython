import FWCore.ParameterSet.Config as cms

def BunchCrossingFilter(*args, **kwargs):
  mod = cms.EDFilter('BunchCrossingFilter',
    bunches = cms.vuint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
