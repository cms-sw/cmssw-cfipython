import FWCore.ParameterSet.Config as cms

printEventSetupContent = cms.EDAnalyzer('PrintEventSetupContent',
  compact = cms.untracked.bool(False),
  printProviders = cms.untracked.bool(True)
)
