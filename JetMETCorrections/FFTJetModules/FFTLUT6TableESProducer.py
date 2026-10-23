import FWCore.ParameterSet.Config as cms

def FFTLUT6TableESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTLUT6TableESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
