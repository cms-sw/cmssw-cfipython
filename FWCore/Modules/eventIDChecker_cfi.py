import FWCore.ParameterSet.Config as cms

eventIDChecker = cms.EDAnalyzer('EventIDChecker',
  multiProcessSequentialEvents = cms.untracked.uint32(0)
)
