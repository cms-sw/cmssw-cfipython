import FWCore.ParameterSet.Config as cms

def TestReadSDSRawDataCollection(*args, **kwargs):
  mod = cms.EDAnalyzer('TestReadSDSRawDataCollection',
    expectedSDSData1 = cms.required.vuint32,
    expectedSDSData2 = cms.required.vuint32,
    sdsRawDataCollectionTag = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
