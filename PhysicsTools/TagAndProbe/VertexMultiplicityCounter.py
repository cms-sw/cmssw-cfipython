import FWCore.ParameterSet.Config as cms

def VertexMultiplicityCounter(**kwargs):
  mod = cms.EDProducer('VertexMultiplicityCounter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
