import FWCore.ParameterSet.Config as cms

def FFTLUT15TableESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTLUT15TableESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
