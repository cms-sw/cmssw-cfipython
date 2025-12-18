import FWCore.ParameterSet.Config as cms

def TestWriteRawDataBuffer(*args, **kwargs):
  mod = cms.EDProducer('TestWriteRawDataBuffer',
    dataPattern1 = cms.required.vuint32,
    dataPattern2 = cms.required.vuint32,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
