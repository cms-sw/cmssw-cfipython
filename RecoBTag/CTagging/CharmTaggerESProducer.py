import FWCore.ParameterSet.Config as cms

def CharmTaggerESProducer(**kwargs):
  mod = cms.ESProducer('CharmTaggerESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
