import FWCore.ParameterSet.Config as cms

def FFTCalo4CorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTCalo4CorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
