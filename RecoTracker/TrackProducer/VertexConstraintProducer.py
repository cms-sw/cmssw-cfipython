import FWCore.ParameterSet.Config as cms

def VertexConstraintProducer(**kwargs):
  mod = cms.EDProducer('VertexConstraintProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
