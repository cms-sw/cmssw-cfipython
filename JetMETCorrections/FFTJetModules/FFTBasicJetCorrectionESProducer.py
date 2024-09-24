import FWCore.ParameterSet.Config as cms

def FFTBasicJetCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTBasicJetCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod