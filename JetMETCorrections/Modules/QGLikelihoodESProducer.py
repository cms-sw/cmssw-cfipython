import FWCore.ParameterSet.Config as cms

def QGLikelihoodESProducer(**kwargs):
  mod = cms.ESProducer('QGLikelihoodESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
