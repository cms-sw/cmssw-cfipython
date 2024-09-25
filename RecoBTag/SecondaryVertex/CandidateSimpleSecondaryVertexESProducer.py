import FWCore.ParameterSet.Config as cms

def CandidateSimpleSecondaryVertexESProducer(*args, **kwargs):
  mod = cms.ESProducer('CandidateSimpleSecondaryVertexESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
