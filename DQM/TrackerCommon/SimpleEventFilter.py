import FWCore.ParameterSet.Config as cms

def SimpleEventFilter(**kwargs):
  mod = cms.EDFilter('SimpleEventFilter',
    DebugOn = cms.untracked.bool(False),
    EventsToSkip = cms.untracked.int32(10),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
