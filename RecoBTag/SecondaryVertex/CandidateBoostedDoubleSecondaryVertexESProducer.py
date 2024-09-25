import FWCore.ParameterSet.Config as cms

def CandidateBoostedDoubleSecondaryVertexESProducer(*args, **kwargs):
  mod = cms.ESProducer('CandidateBoostedDoubleSecondaryVertexESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
