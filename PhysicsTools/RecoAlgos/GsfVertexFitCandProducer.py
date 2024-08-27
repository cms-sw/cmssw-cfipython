import FWCore.ParameterSet.Config as cms

def GsfVertexFitCandProducer(**kwargs):
  mod = cms.EDProducer('GsfVertexFitCandProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
