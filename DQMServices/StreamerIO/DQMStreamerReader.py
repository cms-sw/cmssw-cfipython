import FWCore.ParameterSet.Config as cms

def DQMStreamerReader(**kwargs):
  mod = cms.Source('DQMStreamerReader',
    SelectEvents = cms.required.untracked.vstring,
    minEventsPerLumi = cms.untracked.int32(1),
    skipFirstLumis = cms.untracked.bool(False),
    deleteDatFiles = cms.untracked.bool(False),
    endOfRunKills = cms.untracked.bool(False),
    inputFileTransitionsEachEvent = cms.untracked.bool(False),
    runNumber = cms.required.untracked.uint32,
    datafnPosition = cms.untracked.uint32(3),
    streamLabel = cms.required.untracked.string,
    delayMillis = cms.required.untracked.uint32,
    nextLumiTimeoutMillis = cms.untracked.int32(-1),
    scanOnce = cms.untracked.bool(False),
    runInputDir = cms.required.untracked.string,
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
