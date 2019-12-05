import FWCore.ParameterSet.Config as cms

XMLoutput = cms.OutputModule('XMLOutputModule',
  outputCommands = cms.untracked.vstring('keep *'),
  SelectEvents = cms.untracked.PSet()
)
