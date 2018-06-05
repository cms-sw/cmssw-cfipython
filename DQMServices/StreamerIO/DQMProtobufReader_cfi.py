import FWCore.ParameterSet.Config as cms

source = cms.Source('DQMProtobufReader',
  firstTime = cms.untracked.uint64(1),
  timeBetweenEvents = cms.untracked.uint64(5000000),
  eventCreationDelay = cms.untracked.uint32(0),
  firstEvent = cms.untracked.uint32(1),
  firstLuminosityBlock = cms.untracked.uint32(1),
  firstRun = cms.untracked.uint32(1),
  processingMode = cms.untracked.string('RunsLumisAndEvents'),
  writeStatusFile = cms.untracked.bool(False),
  skipFirstLumis = cms.untracked.bool(False),
  deleteDatFiles = cms.untracked.bool(False),
  endOfRunKills = cms.untracked.bool(False),
  loadFiles = cms.untracked.bool(True),
  datafnPosition = cms.untracked.uint32(3),
  nextLumiTimeoutMillis = cms.untracked.int32(-1),
  scanOnce = cms.untracked.bool(False)
)
