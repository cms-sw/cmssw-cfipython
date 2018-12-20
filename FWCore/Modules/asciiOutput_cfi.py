import FWCore.ParameterSet.Config as cms

asciiOutput = cms.OutputModule('AsciiOutputModule',
  prescale = cms.untracked.uint32(1),
  verbosity = cms.untracked.uint32(1),
  outputCommands = cms.untracked.vstring('keep *'),
  SelectEvents = cms.untracked.PSet()
)
