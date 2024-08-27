import FWCore.ParameterSet.Config as cms

def FFTCalo1CorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTCalo1CorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
