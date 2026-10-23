import FWCore.ParameterSet.Config as cms

def QGLikelihoodESProducer(*args, **kwargs):
  mod = cms.ESProducer('QGLikelihoodESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
