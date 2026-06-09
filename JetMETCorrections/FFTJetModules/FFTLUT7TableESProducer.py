import FWCore.ParameterSet.Config as cms

def FFTLUT7TableESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTLUT7TableESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
