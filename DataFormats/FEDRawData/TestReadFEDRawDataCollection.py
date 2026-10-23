import FWCore.ParameterSet.Config as cms

def TestReadFEDRawDataCollection(*args, **kwargs):
  mod = cms.EDAnalyzer('TestReadFEDRawDataCollection',
    expectedFEDData0 = cms.required.vuint32,
    expectedFEDData3 = cms.required.vuint32,
    fedRawDataCollectionTag = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
