import FWCore.ParameterSet.Config as cms

def EventWithHistoryEDFilter(*args, **kwargs):
  mod = cms.EDFilter('EventWithHistoryEDFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
