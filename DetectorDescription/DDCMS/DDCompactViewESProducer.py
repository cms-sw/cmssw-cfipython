import FWCore.ParameterSet.Config as cms

def DDCompactViewESProducer(**kwargs):
  mod = cms.ESProducer('DDCompactViewESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
