import FWCore.ParameterSet.Config as cms

def LeptonTaggerByPtESProducer(**kwargs):
  mod = cms.ESProducer('LeptonTaggerByPtESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
