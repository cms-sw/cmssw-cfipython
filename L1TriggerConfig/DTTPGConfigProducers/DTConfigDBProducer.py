import FWCore.ParameterSet.Config as cms

def DTConfigDBProducer(**kwargs):
  mod = cms.ESProducer('DTConfigDBProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
