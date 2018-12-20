import FWCore.ParameterSet.Config as cms

source = cms.Source('DQMStreamerReader',
  minEventsPerLumi = cms.untracked.int32(1),
  skipFirstLumis = cms.untracked.bool(False),
  deleteDatFiles = cms.untracked.bool(False),
  endOfRunKills = cms.untracked.bool(False),
  inputFileTransitionsEachEvent = cms.untracked.bool(False),
  datafnPosition = cms.untracked.uint32(3),
  nextLumiTimeoutMillis = cms.untracked.int32(-1),
  scanOnce = cms.untracked.bool(False),
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
