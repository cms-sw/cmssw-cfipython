import FWCore.ParameterSet.Config as cms

tabletestOutput = cms.OutputModule('edmtest::TableTestOutputModule',
  outputCommands = cms.untracked.vstring('keep *'),
  SelectEvents = cms.untracked.PSet()
)
