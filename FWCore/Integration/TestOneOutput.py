import FWCore.ParameterSet.Config as cms

def TestOneOutput(**kwargs):
  mod = cms.OutputModule('TestOneOutput',
    outputCommands = cms.untracked.vstring('keep *'),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.optional.vstring
    ),
    verbose = cms.untracked.bool(True),
    expectedProcessesWithProcessBlockProducts = cms.untracked.vstring(),
    expectedTopProcessesWithProcessBlockProducts = cms.untracked.vstring(),
    expectedAddedProcesses = cms.untracked.vstring('DONOTTEST'),
    expectedTopAddedProcesses = cms.untracked.vstring('DONOTTEST'),
    expectedTopCacheIndices0 = cms.untracked.vuint32(),
    expectedTopCacheIndices1 = cms.untracked.vuint32(),
    expectedTopCacheIndices2 = cms.untracked.vuint32(),
    expectedProcessNamesAtWrite = cms.untracked.vstring(),
    expectedWriteProcessBlockTransitions = cms.untracked.int32(-1),
    requireNullTTreesInFileBlock = cms.untracked.bool(False),
    testTTreesInFileBlock = cms.untracked.bool(False),
    expectedCacheIndexSize = cms.untracked.vuint32(),
    expectedProcessesInFirstFile = cms.untracked.uint32(0),
    expectedCacheIndexVectorsPerFile = cms.untracked.vuint32(),
    expectedNEntries0 = cms.untracked.vuint32(),
    expectedNEntries1 = cms.untracked.vuint32(),
    expectedNEntries2 = cms.untracked.vuint32(),
    expectedCacheEntriesPerFile0 = cms.untracked.vuint32(),
    expectedCacheEntriesPerFile1 = cms.untracked.vuint32(),
    expectedCacheEntriesPerFile2 = cms.untracked.vuint32(),
    expectedOuterOffset = cms.untracked.vuint32(),
    expectedTranslateFromStoredIndex = cms.untracked.vuint32(),
    expectedNAddedProcesses = cms.untracked.uint32(4294967295),
    expectedProductsFromInputKept = cms.untracked.bool(True)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
