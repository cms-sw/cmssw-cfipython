import FWCore.ParameterSet.Config as cms

source = cms.Source('EmptySource',
  firstTime = cms.untracked.uint64(1),
  timeBetweenEvents = cms.untracked.uint64(5000000),
  eventCreationDelay = cms.untracked.uint32(0),
  firstEvent = cms.untracked.uint32(1),
  firstLuminosityBlock = cms.untracked.uint32(1),
  firstRun = cms.untracked.uint32(1),
  processingMode = cms.untracked.string('RunsLumisAndEvents'),
  writeStatusFile = cms.untracked.bool(False)
)
