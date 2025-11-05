import FWCore.ParameterSet.Config as cms

def RNTupleTempOutputModule(*args, **kwargs):
  mod = cms.OutputModule('RNTupleTempOutputModule',
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
    fastCloning = cms.untracked.bool(False),
    mergeJob = cms.untracked.bool(False),
    compactEventAuxiliary = cms.untracked.bool(False),
    overrideInputFileSplitLevels = cms.untracked.bool(False),
    writeStatusFile = cms.untracked.bool(False),
    dropMetaData = cms.untracked.string(''),
    overrideGUID = cms.untracked.string(''),
    dataset = cms.untracked.PSet(),
    overrideBranchesSplitLevel = cms.untracked.VPSet(
      template = cms.PSetTemplate(
        branch = cms.optional.untracked.string,
        splitLevel = cms.optional.untracked.int32
      )
    ),
    branchAliases = cms.untracked.VPSet(
      template = cms.PSetTemplate(
        branch = cms.optional.untracked.string,
        alias = cms.optional.untracked.string
      )
    ),
    rntupleWriteOptions = cms.untracked.PSet(
      approxZippedClusterSize = cms.untracked.uint64(134217728),
      maxUnzippedClusterSize = cms.untracked.uint64(1342177280),
      initialUnzippedPageSize = cms.untracked.uint64(256),
      maxUnzippedPageSize = cms.untracked.uint64(1048576),
      pageBufferBudget = cms.untracked.uint64(0),
      useBufferedWrite = cms.untracked.bool(True),
      useDirectIO = cms.untracked.bool(False)
    ),
    fieldLevelOptimizations = cms.untracked.PSet(
      noSplitSubFields = cms.untracked.vstring(),
      useStreamer = cms.untracked.bool(False),
      overrideDataProductStreamer = cms.untracked.VPSet(
        template = cms.PSetTemplate(
          product = cms.required.untracked.string,
          useStreamer = cms.untracked.bool(True)
        )
      )
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
