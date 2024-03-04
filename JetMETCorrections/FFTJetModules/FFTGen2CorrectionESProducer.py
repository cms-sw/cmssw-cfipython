import FWCore.ParameterSet.Config as cms

def FFTGen2CorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTGen2CorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
