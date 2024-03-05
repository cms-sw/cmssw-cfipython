import FWCore.ParameterSet.Config as cms

def GTTFileReader(**kwargs):
  mod = cms.EDProducer('GTTFileReader',
    processOutputToCorrelator = cms.required.bool,
    processInputTracks = cms.required.bool,
    processOutputToGlobalTrigger = cms.required.bool,
    kEmptyFramesOutputToCorrelator = cms.untracked.uint32(0),
    kEmptyFramesInputTracks = cms.untracked.uint32(0),
    kEmptyFramesOutputToGlobalTrigger = cms.untracked.uint32(0),
    filesOutputToCorrelator = cms.vstring('L1GTTOutputToCorrelator_0.txt'),
    filesInputTracks = cms.vstring('L1GTTInputFile_0.txt'),
    filesOutputToGlobalTrigger = cms.vstring('L1GTTOutputToGlobalTriggerFile_0.txt'),
    format = cms.untracked.string('APx'),
    l1VertexCollectionName = cms.string('L1VerticesFirmware'),
    l1TrackCollectionName = cms.string('Level1TTTracks'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
