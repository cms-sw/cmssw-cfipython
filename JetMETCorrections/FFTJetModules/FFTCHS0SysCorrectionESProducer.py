import FWCore.ParameterSet.Config as cms

def FFTCHS0SysCorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTCHS0SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
