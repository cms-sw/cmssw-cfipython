import FWCore.ParameterSet.Config as cms

def FFTCalo6SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTCalo6SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
