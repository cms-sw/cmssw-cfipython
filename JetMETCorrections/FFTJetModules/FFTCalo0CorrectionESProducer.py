import FWCore.ParameterSet.Config as cms

def FFTCalo0CorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTCalo0CorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
