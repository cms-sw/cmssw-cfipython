import FWCore.ParameterSet.Config as cms

def FFTCHS7SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTCHS7SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod