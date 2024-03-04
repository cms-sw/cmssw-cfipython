import FWCore.ParameterSet.Config as cms

def FFTGenJetSysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTGenJetSysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
