import FWCore.ParameterSet.Config as cms

PrintEventSetupDataRetrieval = cms.Service('PrintEventSetupDataRetrieval',
  printProviders = cms.untracked.bool(False),
  checkAfterBeginRun = cms.untracked.bool(False),
  checkAfterBeginLumi = cms.untracked.bool(False),
  checkAfterEvent = cms.untracked.bool(True)
)
