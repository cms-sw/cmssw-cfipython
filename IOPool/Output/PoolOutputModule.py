import FWCore.ParameterSet.Config as cms

def PoolOutputModule(*args, **kwargs):
  mod = cms.OutputModule('PoolOutputModule',
    fileName = cms.required.untracked.string,
    logicalFileName = cms.untracked.string(''),
    catalog = cms.untracked.string(''),
    maxSize = cms.untracked.int32(2130706432),
    compressionLevel = cms.untracked.int32(4),
    compressionAlgorithm = cms.untracked.string('ZSTD'),
    basketSize = cms.untracked.int32(16384),
    eventAuxiliaryBasketSize = cms.untracked.int32(16384),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    splitLevel = cms.untracked.int32(99),
    sortBaskets = cms.untracked.string('sortbasketsbyoffset'),
    treeMaxVirtualSize = cms.untracked.int32(-1),
    fastCloning = cms.untracked.bool(True),
    mergeJob = cms.untracked.bool(False),
    compactEventAuxiliary = cms.untracked.bool(False),
    overrideInputFileSplitLevels = cms.untracked.bool(False),
    writeStatusFile = cms.untracked.bool(False),
    dropMetaData = cms.untracked.string(''),
    overrideGUID = cms.untracked.string(''),
    dataset = cms.untracked.PSet(),
    overrideBranchesSplitLevel = cms.untracked.VPSet(
    ),
    outputCommands = cms.untracked.vstring('keep *'),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.optional.vstring
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
