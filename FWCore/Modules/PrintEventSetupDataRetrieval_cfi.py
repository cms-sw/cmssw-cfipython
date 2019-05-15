import FWCore.ParameterSet.Config as cms

PrintEventSetupDataRetrieval = cms.EDAnalyzer('PrintEventSetupDataRetrieval',
  printProviders = cms.untracked.bool(False),
  checkDuringBeginRun = cms.untracked.bool(False),
  checkDuringBeginLumi = cms.untracked.bool(False),
  checkDuringEvent = cms.untracked.bool(True)
)
