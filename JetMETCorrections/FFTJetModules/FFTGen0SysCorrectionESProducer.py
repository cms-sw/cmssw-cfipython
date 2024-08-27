import FWCore.ParameterSet.Config as cms

def FFTGen0SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTGen0SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
