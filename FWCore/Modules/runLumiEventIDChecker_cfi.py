import FWCore.ParameterSet.Config as cms

runLumiEventIDChecker = cms.EDAnalyzer('RunLumiEventChecker',
  eventSequence = cms.required.untracked.VEventID,
  unorderedEvents = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)
