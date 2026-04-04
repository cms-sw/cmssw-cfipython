import FWCore.ParameterSet.Config as cms

def KalmanVertexFitCompositeCandProducer(*args, **kwargs):
  mod = cms.EDProducer('KalmanVertexFitCompositeCandProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
