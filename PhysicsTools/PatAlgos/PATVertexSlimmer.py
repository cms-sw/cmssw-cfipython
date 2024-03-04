import FWCore.ParameterSet.Config as cms

def PATVertexSlimmer(**kwargs):
  mod = cms.EDProducer('PATVertexSlimmer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
