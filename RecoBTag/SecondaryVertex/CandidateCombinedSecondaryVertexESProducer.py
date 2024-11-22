import FWCore.ParameterSet.Config as cms

def CandidateCombinedSecondaryVertexESProducer(*args, **kwargs):
  mod = cms.ESProducer('CandidateCombinedSecondaryVertexESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
