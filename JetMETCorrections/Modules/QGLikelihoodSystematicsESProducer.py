import FWCore.ParameterSet.Config as cms

def QGLikelihoodSystematicsESProducer(**kwargs):
  mod = cms.ESProducer('QGLikelihoodSystematicsESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
