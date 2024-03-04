import FWCore.ParameterSet.Config as cms

def DQMProtobufReader(**kwargs):
  mod = cms.Source('DQMProtobufReader',
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
    skipFirstLumis = cms.untracked.bool(False),
    deleteDatFiles = cms.untracked.bool(False),
    endOfRunKills = cms.untracked.bool(False),
    loadFiles = cms.untracked.bool(True),
    runNumber = cms.required.untracked.uint32,
    datafnPosition = cms.untracked.uint32(3),
    streamLabel = cms.required.untracked.string,
    delayMillis = cms.required.untracked.uint32,
    nextLumiTimeoutMillis = cms.untracked.int32(-1),
    scanOnce = cms.untracked.bool(False),
    runInputDir = cms.required.untracked.string
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
