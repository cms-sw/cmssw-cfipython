import FWCore.ParameterSet.Config as cms

def RNTupleOutputModule(*args, **kwargs):
  mod = cms.OutputModule('RNTupleOutputModule',
    fileName = cms.required.untracked.string,
    compressionAlgorithm = cms.untracked.string('ZSTD'),
    compressionLevel = cms.untracked.int32(4),
    approxZippedClusterSize = cms.untracked.uint64(134217728),
    maxUnzippedClusterSize = cms.untracked.uint64(1342177280),
    initialUnzippedPageSize = cms.untracked.uint64(256),
    maxUnzippedPageSize = cms.untracked.uint64(1048576),
    pageBufferBudget = cms.untracked.uint64(0),
    useBufferedWrite = cms.untracked.bool(True),
    useDirectIO = cms.untracked.bool(False),
    dropPerEventDataProductProvenance = cms.untracked.bool(False),
    noSplitSubFields = cms.untracked.vstring(),
    useStreamer = cms.untracked.bool(False),
    overrideDataProductStreamer = cms.untracked.VPSet(
      template = cms.PSetTemplate(
        product = cms.required.untracked.string,
        useStreamer = cms.untracked.bool(True)
      )
    ),
    outputCommands = cms.untracked.vstring('keep *'),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.optional.vstring
    ),
    logicalFileName = cms.untracked.string(''),
    catalog = cms.untracked.string(''),
    maxSize = cms.untracked.int32(2130706432),
    basketSize = cms.obsolete.untracked.int32,
    eventAuxiliaryBasketSize = cms.obsolete.untracked.int32,
    eventAutoFlushCompressedSize = cms.obsolete.untracked.int32,
    splitLevel = cms.obsolete.untracked.int32,
    sortBaskets = cms.obsolete.untracked.string,
    treeMaxVirtualSize = cms.obsolete.untracked.int32,
    fastCloning = cms.untracked.bool(False),
    mergeJob = cms.optional.untracked.bool,
    compactEventAuxiliary = cms.obsolete.untracked.bool,
    overrideInputFileSplitLevels = cms.obsolete.untracked.bool,
    writeStatusFile = cms.untracked.bool(False),
    dropMetaData = cms.untracked.string(''),
    overrideGUID = cms.untracked.string(''),
    dataset = cms.untracked.PSet(),
    overrideBranchesSplitLevel = cms.obsolete.untracked.VPSet,
    branchAliases = cms.obsolete.untracked.VPSet
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
