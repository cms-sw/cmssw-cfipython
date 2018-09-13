import FWCore.ParameterSet.Config as cms

jsonWriting = cms.OutputModule('JsonWritingTimeoutPoolOutputModule',
  logicalFileName = cms.untracked.string(''),
  catalog = cms.untracked.string(''),
  maxSize = cms.untracked.int32(2130706432),
  compressionLevel = cms.untracked.int32(7),
  compressionAlgorithm = cms.untracked.string('ZLIB'),
  basketSize = cms.untracked.int32(16384),
  eventAutoFlushCompressedSize = cms.untracked.int32(-1),
  splitLevel = cms.untracked.int32(99),
  sortBaskets = cms.untracked.string('sortbasketsbyoffset'),
  treeMaxVirtualSize = cms.untracked.int32(-1),
  fastCloning = cms.untracked.bool(True),
  overrideInputFileSplitLevels = cms.untracked.bool(False),
  writeStatusFile = cms.untracked.bool(False),
  dropMetaData = cms.untracked.string(''),
  dataset = cms.untracked.PSet(),
  outputCommands = cms.untracked.vstring('keep *'),
  SelectEvents = cms.untracked.PSet(),
  runNumber = cms.untracked.uint32(0),
  outputPath = cms.untracked.string('./'),
  streamLabel = cms.untracked.string('streamEvDOutput')
)
