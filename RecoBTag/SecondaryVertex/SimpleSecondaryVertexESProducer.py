import FWCore.ParameterSet.Config as cms

def SimpleSecondaryVertexESProducer(*args, **kwargs):
  mod = cms.ESProducer('SimpleSecondaryVertexESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
