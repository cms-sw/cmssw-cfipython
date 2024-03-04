import FWCore.ParameterSet.Config as cms

def FFTCalo1SysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTCalo1SysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
