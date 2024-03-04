import FWCore.ParameterSet.Config as cms

def FFTCalo5SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTCalo5SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
