import FWCore.ParameterSet.Config as cms

_simpleEventFilter = cms.EDFilter('SimpleEventFilter',
  DebugOn = cms.untracked.bool(False),
  EventsToSkip = cms.untracked.int32(10),
  mightGet = cms.optional.untracked.vstring
)
