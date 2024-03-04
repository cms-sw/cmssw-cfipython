import FWCore.ParameterSet.Config as cms

def FFTGen0CorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTGen0CorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
