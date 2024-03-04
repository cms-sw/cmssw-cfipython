import FWCore.ParameterSet.Config as cms

def TestReadSDSRawDataCollection(**kwargs):
  mod = cms.EDAnalyzer('TestReadSDSRawDataCollection',
    expectedSDSData1 = cms.required.vuint32,
    expectedSDSData2 = cms.required.vuint32,
    sdsRawDataCollectionTag = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
