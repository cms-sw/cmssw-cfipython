import FWCore.ParameterSet.Config as cms

def DDCompactViewMFESProducer(**kwargs):
  mod = cms.ESProducer('DDCompactViewMFESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
