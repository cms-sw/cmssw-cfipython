import FWCore.ParameterSet.Config as cms

def TestReadFEDRawDataCollection(**kwargs):
  mod = cms.EDAnalyzer('TestReadFEDRawDataCollection',
    expectedFEDData0 = cms.required.vuint32,
    expectedFEDData3 = cms.required.vuint32,
    fedRawDataCollectionTag = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
