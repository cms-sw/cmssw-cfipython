import FWCore.ParameterSet.Config as cms

source = cms.Source('TestSource',
  numberEventsInRun = cms.optional.untracked.uint32,
  numberEventsInLuminosityBlock = cms.optional.untracked.uint32,
  firstTime = cms.untracked.uint64(1),
  timeBetweenEvents = cms.untracked.uint64(5000000),
  eventCreationDelay = cms.untracked.uint32(0),
  firstEvent = cms.untracked.uint32(1),
  firstLuminosityBlock = cms.untracked.uint32(1),
  firstRun = cms.untracked.uint32(1),
  firstLuminosityBlockForEachRun = cms.untracked.VLuminosityBlockID(),
  processingMode = cms.untracked.string('RunsLumisAndEvents'),
  writeStatusFile = cms.untracked.bool(False),
  transitions = cms.untracked.VPSet(
    cms.PSet()
  )
)
