import FWCore.ParameterSet.Config as cms

def FFTCalo2CorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTCalo2CorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
