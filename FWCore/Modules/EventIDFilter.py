import FWCore.ParameterSet.Config as cms

def EventIDFilter(*args, **kwargs):
  mod = cms.EDFilter('EventIDFilter',
    eventsToPass = cms.required.VEventID,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
