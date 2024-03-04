import FWCore.ParameterSet.Config as cms

def FFTBasicJetSysCorrectionESProducer(**kwargs):
  mod = cms.ESProducer('FFTBasicJetSysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
