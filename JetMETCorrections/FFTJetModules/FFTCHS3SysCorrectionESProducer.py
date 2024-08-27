import FWCore.ParameterSet.Config as cms

def FFTCHS3SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTCHS3SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
