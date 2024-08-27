import FWCore.ParameterSet.Config as cms

def SimpleSecondaryVertexESProducer(**kwargs):
  mod = cms.ESProducer('SimpleSecondaryVertexESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
