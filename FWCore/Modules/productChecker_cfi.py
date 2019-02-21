import FWCore.ParameterSet.Config as cms

productChecker = cms.OutputModule('GetProductCheckerOutputModule',
  outputCommands = cms.untracked.vstring('keep *'),
  SelectEvents = cms.untracked.PSet()
)
