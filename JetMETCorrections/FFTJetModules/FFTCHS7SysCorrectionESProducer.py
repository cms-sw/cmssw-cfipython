import FWCore.ParameterSet.Config as cms

def FFTCHS7SysCorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTCHS7SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
