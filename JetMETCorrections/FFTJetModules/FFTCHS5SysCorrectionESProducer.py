import FWCore.ParameterSet.Config as cms

def FFTCHS5SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTCHS5SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
