import FWCore.ParameterSet.Config as cms

def FFTCalo8SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTCalo8SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
