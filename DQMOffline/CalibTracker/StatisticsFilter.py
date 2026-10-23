import FWCore.ParameterSet.Config as cms

def StatisticsFilter(*args, **kwargs):
  mod = cms.EDFilter('StatisticsFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
