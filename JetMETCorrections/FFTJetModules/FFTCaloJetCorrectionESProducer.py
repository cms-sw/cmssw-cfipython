import FWCore.ParameterSet.Config as cms

def FFTCaloJetCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTCaloJetCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
