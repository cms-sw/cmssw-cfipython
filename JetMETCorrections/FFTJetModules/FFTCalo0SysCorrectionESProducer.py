import FWCore.ParameterSet.Config as cms

def FFTCalo0SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTCalo0SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
