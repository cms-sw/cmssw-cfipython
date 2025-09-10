import FWCore.ParameterSet.Config as cms

def KalmanVertexFitCandProducer(*args, **kwargs):
  mod = cms.EDProducer('KalmanVertexFitCandProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
