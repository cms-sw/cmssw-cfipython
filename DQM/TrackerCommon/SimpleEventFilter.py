import FWCore.ParameterSet.Config as cms

def SimpleEventFilter(*args, **kwargs):
  mod = cms.EDFilter('SimpleEventFilter',
    DebugOn = cms.untracked.bool(False),
    EventsToSkip = cms.untracked.int32(10),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
