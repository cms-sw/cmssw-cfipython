import FWCore.ParameterSet.Config as cms

def FFTCalo3CorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTCalo3CorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
