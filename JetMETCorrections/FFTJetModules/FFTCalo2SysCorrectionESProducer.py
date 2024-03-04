import FWCore.ParameterSet.Config as cms

def FFTCalo2SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTCalo2SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
