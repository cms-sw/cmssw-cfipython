import FWCore.ParameterSet.Config as cms

def FFTCalo3SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTCalo3SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
