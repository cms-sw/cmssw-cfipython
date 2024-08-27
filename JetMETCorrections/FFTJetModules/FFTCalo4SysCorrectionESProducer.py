import FWCore.ParameterSet.Config as cms

def FFTCalo4SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTCalo4SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
