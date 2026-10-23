import FWCore.ParameterSet.Config as cms

def TestWriteSDSRawDataCollection(*args, **kwargs):
  mod = cms.EDProducer('TestWriteSDSRawDataCollection',
    SDSData1 = cms.required.vuint32,
    SDSData2 = cms.required.vuint32,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
