import FWCore.ParameterSet.Config as cms

def NewEventStreamFileReader(**kwargs):
  mod = cms.Source('NewEventStreamFileReader',
    fileNames = cms.required.untracked.vstring,
    skipEvents = cms.untracked.uint32(0),
    overrideCatalog = cms.untracked.string(''),
    inputFileTransitionsEachEvent = cms.untracked.bool(False),
    prefetchMBytes = cms.untracked.uint32(0),
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