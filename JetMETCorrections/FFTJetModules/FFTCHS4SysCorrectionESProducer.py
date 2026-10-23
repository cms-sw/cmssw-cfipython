import FWCore.ParameterSet.Config as cms

def FFTCHS4SysCorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTCHS4SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
