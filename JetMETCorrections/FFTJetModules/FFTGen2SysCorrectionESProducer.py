import FWCore.ParameterSet.Config as cms

def FFTGen2SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTGen2SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
