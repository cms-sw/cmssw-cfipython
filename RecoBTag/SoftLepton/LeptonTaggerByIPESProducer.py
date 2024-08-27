import FWCore.ParameterSet.Config as cms

def LeptonTaggerByIPESProducer(**kwargs):
  mod = cms.ESProducer('LeptonTaggerByIPESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
