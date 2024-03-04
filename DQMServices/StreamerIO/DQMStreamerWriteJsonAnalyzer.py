import FWCore.ParameterSet.Config as cms

def DQMStreamerWriteJsonAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('DQMStreamerWriteJsonAnalyzer',
    eventsPerLumi = cms.required.untracked.uint32,
    runNumber = cms.required.untracked.uint32,
    streamName = cms.required.untracked.string,
    pathToWriteJson = cms.required.untracked.string,
    dataFileForEachLumi = cms.required.untracked.vstring,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
