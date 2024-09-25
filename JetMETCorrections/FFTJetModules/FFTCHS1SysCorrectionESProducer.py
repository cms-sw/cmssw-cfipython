import FWCore.ParameterSet.Config as cms

def FFTCHS1SysCorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTCHS1SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
