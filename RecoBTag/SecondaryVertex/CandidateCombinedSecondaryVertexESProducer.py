import FWCore.ParameterSet.Config as cms

def CandidateCombinedSecondaryVertexESProducer(**kwargs):
  mod = cms.ESProducer('CandidateCombinedSecondaryVertexESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
