import FWCore.ParameterSet.Config as cms

def FFTGen1CorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTGen1CorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
