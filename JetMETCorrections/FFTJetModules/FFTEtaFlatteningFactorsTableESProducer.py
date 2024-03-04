import FWCore.ParameterSet.Config as cms

def FFTEtaFlatteningFactorsTableESProducer(**kwargs):
  mod = cms.ESProducer('FFTEtaFlatteningFactorsTableESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
