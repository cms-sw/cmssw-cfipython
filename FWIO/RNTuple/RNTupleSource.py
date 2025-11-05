import FWCore.ParameterSet.Config as cms

def RNTupleSource(*args, **kwargs):
  mod = cms.Source('RNTupleSource',
    fileNames = cms.required.untracked.vstring,
    enableMetrics = cms.untracked.bool(False),
    useClusterCache = cms.untracked.bool(True),
    secondaryFileNames = cms.optional.untracked.vstring,
    needSecondaryFileNames = cms.optional.untracked.bool,
    overrideCatalog = cms.optional.untracked.string,
    skipBadFiles = cms.optional.untracked.bool,
    bypassVersionCheck = cms.optional.untracked.bool,
    treeMaxVirtualSize = cms.obsolete.untracked.int32,
    dropDescendantsOfDroppedBranches = cms.optional.untracked.bool,
    labelRawDataLikeMC = cms.optional.untracked.bool,
    delayReadingEventProducts = cms.optional.untracked.bool,
    firstLuminosityBlock = cms.optional.untracked.uint32,
    inputCommands = cms.untracked.vstring('keep *'),
    processingMode = cms.untracked.string('RunsLumisAndEvents'),
    writeStatusFile = cms.untracked.bool(False),
    setRunNumber = cms.untracked.uint32(0)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
