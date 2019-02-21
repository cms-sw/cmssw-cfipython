import FWCore.ParameterSet.Config as cms

source = cms.Source('NewEventStreamFileReader',
  skipEvents = cms.untracked.uint32(0),
  overrideCatalog = cms.untracked.string(''),
  inputFileTransitionsEachEvent = cms.untracked.bool(False),
  processingMode = cms.untracked.string('RunsLumisAndEvents'),
  writeStatusFile = cms.untracked.bool(False),
  firstRun = cms.untracked.uint32(1),
  firstLuminosityBlock = cms.untracked.uint32(0),
  firstEvent = cms.untracked.uint32(1),
  lumisToSkip = cms.untracked.VLuminosityBlockRange(),
  lumisToProcess = cms.untracked.VLuminosityBlockRange(),
  eventsToSkip = cms.untracked.VEventRange(),
  eventsToProcess = cms.untracked.VEventRange()
)
