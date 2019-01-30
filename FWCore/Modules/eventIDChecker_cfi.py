import FWCore.ParameterSet.Config as cms

eventIDChecker = cms.EDAnalyzer('MulticoreRunLumiEventChecker',
  multiProcessSequentialEvents = cms.untracked.uint32(0)
)
