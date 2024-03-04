import FWCore.ParameterSet.Config as cms

def LeptonTaggerByDistanceESProducer(**kwargs):
  mod = cms.ESProducer('LeptonTaggerByDistanceESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
