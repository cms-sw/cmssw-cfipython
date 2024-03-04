import FWCore.ParameterSet.Config as cms

def FFTCHS8SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTCHS8SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
