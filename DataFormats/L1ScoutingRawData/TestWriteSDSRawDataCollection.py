import FWCore.ParameterSet.Config as cms

def TestWriteSDSRawDataCollection(**kwargs):
  mod = cms.EDProducer('TestWriteSDSRawDataCollection',
    SDSData1 = cms.required.vuint32,
    SDSData2 = cms.required.vuint32,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
