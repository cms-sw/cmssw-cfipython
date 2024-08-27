import FWCore.ParameterSet.Config as cms

def FastPrimaryVertexProducer(**kwargs):
  mod = cms.EDProducer('FastPrimaryVertexProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
