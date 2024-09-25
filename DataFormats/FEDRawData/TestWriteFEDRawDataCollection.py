import FWCore.ParameterSet.Config as cms

def TestWriteFEDRawDataCollection(*args, **kwargs):
  mod = cms.EDProducer('TestWriteFEDRawDataCollection',
    FEDData0 = cms.required.vuint32,
    FEDData3 = cms.required.vuint32,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
