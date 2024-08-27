import FWCore.ParameterSet.Config as cms

def FFTCalo9SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTCalo9SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
