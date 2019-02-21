import FWCore.ParameterSet.Config as cms

provenanceChecker = cms.OutputModule('ProvenanceCheckerOutputModule',
  outputCommands = cms.untracked.vstring('keep *'),
  SelectEvents = cms.untracked.PSet()
)
