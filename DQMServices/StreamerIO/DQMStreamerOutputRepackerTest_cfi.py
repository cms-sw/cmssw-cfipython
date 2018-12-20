import FWCore.ParameterSet.Config as cms

DQMStreamerOutputRepackerTest = cms.OutputModule('DQMStreamerOutputRepackerTest',
  max_event_size = cms.untracked.int32(7000000),
  use_compression = cms.untracked.bool(True),
  compression_level = cms.untracked.int32(1),
  lumiSection_interval = cms.untracked.int32(0),
  outputCommands = cms.untracked.vstring('keep *'),
  SelectEvents = cms.untracked.PSet(),
  outputPath = cms.untracked.string('./output/'),
  streamLabel = cms.untracked.string('DQM')
)
