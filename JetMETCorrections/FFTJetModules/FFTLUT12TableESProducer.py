import FWCore.ParameterSet.Config as cms

def FFTLUT12TableESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTLUT12TableESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
