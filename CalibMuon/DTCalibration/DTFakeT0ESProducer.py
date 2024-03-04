import FWCore.ParameterSet.Config as cms

def DTFakeT0ESProducer(**kwargs):
  mod = cms.ESSource('DTFakeT0ESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
