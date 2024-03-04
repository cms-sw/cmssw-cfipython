import FWCore.ParameterSet.Config as cms

def KalmanVertexFitCompositeCandProducer(**kwargs):
  mod = cms.EDProducer('KalmanVertexFitCompositeCandProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
