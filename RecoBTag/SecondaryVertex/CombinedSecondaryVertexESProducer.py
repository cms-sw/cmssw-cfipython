import FWCore.ParameterSet.Config as cms

def CombinedSecondaryVertexESProducer(*args, **kwargs):
  mod = cms.ESProducer('CombinedSecondaryVertexESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
