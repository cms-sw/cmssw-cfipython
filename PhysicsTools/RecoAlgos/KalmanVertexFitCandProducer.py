import FWCore.ParameterSet.Config as cms

def KalmanVertexFitCandProducer(**kwargs):
  mod = cms.EDProducer('KalmanVertexFitCandProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
