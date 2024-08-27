import FWCore.ParameterSet.Config as cms

def TestWriteFEDRawDataCollection(**kwargs):
  mod = cms.EDProducer('TestWriteFEDRawDataCollection',
    FEDData0 = cms.required.vuint32,
    FEDData3 = cms.required.vuint32,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
