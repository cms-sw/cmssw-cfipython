import FWCore.ParameterSet.Config as cms

eventIDChecker = cms.EDAnalyzer('EventIDChecker',
  eventSequence = cms.required.untracked.VEventID,
  multiProcessSequentialEvents = cms.untracked.uint32(0),
  mightGet = cms.optional.untracked.vstring
)
