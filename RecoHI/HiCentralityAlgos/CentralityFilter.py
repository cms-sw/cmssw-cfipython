import FWCore.ParameterSet.Config as cms

def CentralityFilter(*args, **kwargs):
  mod = cms.EDFilter('CentralityFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
