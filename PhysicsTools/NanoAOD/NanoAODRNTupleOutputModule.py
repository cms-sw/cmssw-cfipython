import FWCore.ParameterSet.Config as cms

def NanoAODRNTupleOutputModule(*args, **kwargs):
  mod = cms.OutputModule('NanoAODRNTupleOutputModule',
    fileName = cms.required.untracked.string,
    logicalFileName = cms.untracked.string(''),
    compressionLevel = cms.untracked.int32(9),
    compressionAlgorithm = cms.untracked.string('ZLIB'),
    noSplitFields = cms.untracked.vstring(),
    rntupleWriteOptions = cms.untracked.PSet(
      approxZippedClusterSize = cms.untracked.uint64(134217728),
      maxUnzippedClusterSize = cms.untracked.uint64(1342177280),
      initialUnzippedPageSize = cms.untracked.uint64(256),
      maxUnzippedPageSize = cms.untracked.uint64(1048576),
      pageBufferBudget = cms.untracked.uint64(0),
      useBufferedWrite = cms.untracked.bool(True),
      useDirectIO = cms.untracked.bool(False)
    ),
    saveProvenance = cms.untracked.bool(True),
    saveTriggerResults = cms.untracked.bool(True),
    outputCommands = cms.untracked.vstring(
      'drop *',
      'keep nanoaodFlatTable_*Table_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep String_*_genModel_*',
      'keep nanoaodMergeableCounterTable_*Table_*_*',
      'keep nanoaodUniqueString_nanoMetadata_*_*'
    ),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.optional.vstring
    ),
    dataset = cms.untracked.PSet(),
    branches = cms.PSet()
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
