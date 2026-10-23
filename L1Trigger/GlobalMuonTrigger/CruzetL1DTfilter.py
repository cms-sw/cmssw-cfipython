import FWCore.ParameterSet.Config as cms

def CruzetL1DTfilter(*args, **kwargs):
  mod = cms.EDFilter('CruzetL1DTfilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
