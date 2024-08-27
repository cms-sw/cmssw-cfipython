import FWCore.ParameterSet.Config as cms

def CandidateBoostedDoubleSecondaryVertexESProducer(**kwargs):
  mod = cms.ESProducer('CandidateBoostedDoubleSecondaryVertexESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
