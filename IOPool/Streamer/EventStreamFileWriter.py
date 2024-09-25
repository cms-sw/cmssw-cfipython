import FWCore.ParameterSet.Config as cms

def EventStreamFileWriter(*args, **kwargs):
  mod = cms.OutputModule('EventStreamFileWriter',
    max_event_size = cms.untracked.int32(7000000),
    use_compression = cms.untracked.bool(True),
    compression_algorithm = cms.untracked.string('ZLIB'),
    compression_level = cms.untracked.int32(1),
    lumiSection_interval = cms.untracked.int32(0),
    outputCommands = cms.untracked.vstring('keep *'),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.optional.vstring
    ),
    psetMap = cms.untracked.InputTag('hltPSetMap'),
    fileName = cms.untracked.string('teststreamfile.dat'),
    padding = cms.untracked.uint32(0)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
