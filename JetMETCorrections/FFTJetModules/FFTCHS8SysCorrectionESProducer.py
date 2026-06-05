import FWCore.ParameterSet.Config as cms

def FFTCHS8SysCorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTCHS8SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
