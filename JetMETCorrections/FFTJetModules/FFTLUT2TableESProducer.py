import FWCore.ParameterSet.Config as cms

def FFTLUT2TableESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTLUT2TableESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
