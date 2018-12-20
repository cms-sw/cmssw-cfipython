import FWCore.ParameterSet.Config as cms

sewerModule = cms.OutputModule('SewerModule',
  outputCommands = cms.untracked.vstring('drop *'),
  SelectEvents = cms.untracked.PSet()
)
