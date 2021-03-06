import FWCore.ParameterSet.Config as cms

source = cms.Source('PoolSource',
  fileNames = cms.required.untracked.vstring,
  secondaryFileNames = cms.untracked.vstring(),
  needSecondaryFileNames = cms.untracked.bool(False),
  overrideCatalog = cms.untracked.string(''),
  skipBadFiles = cms.untracked.bool(False),
  bypassVersionCheck = cms.untracked.bool(False),
  treeMaxVirtualSize = cms.untracked.int32(-1),
  dropDescendantsOfDroppedBranches = cms.untracked.bool(True),
  labelRawDataLikeMC = cms.untracked.bool(True),
  delayReadingEventProducts = cms.untracked.bool(True),
  inputCommands = cms.untracked.vstring('keep *'),
  processingMode = cms.untracked.string('RunsLumisAndEvents'),
  writeStatusFile = cms.untracked.bool(False),
  skipEvents = cms.untracked.uint32(0),
  noEventSort = cms.untracked.bool(True),
  cacheSize = cms.untracked.uint32(20971520),
  branchesMustMatch = cms.untracked.string('permissive'),
  enforceGUIDInFileName = cms.untracked.bool(False),
  firstRun = cms.untracked.uint32(1),
  firstLuminosityBlock = cms.untracked.uint32(0),
  firstEvent = cms.untracked.uint32(1),
  lumisToSkip = cms.untracked.VLuminosityBlockRange(),
  lumisToProcess = cms.untracked.VLuminosityBlockRange(),
  eventsToSkip = cms.untracked.VEventRange(),
  eventsToProcess = cms.untracked.VEventRange(),
  duplicateCheckMode = cms.untracked.string('checkAllFilesOpened'),
  setRunNumber = cms.untracked.uint32(0)
)
