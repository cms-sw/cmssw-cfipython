import FWCore.ParameterSet.Config as cms

def FFTGenJetCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTGenJetCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
