import FWCore.ParameterSet.Config as cms

def CombinedSecondaryVertexESProducer(**kwargs):
  mod = cms.ESProducer('CombinedSecondaryVertexESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
