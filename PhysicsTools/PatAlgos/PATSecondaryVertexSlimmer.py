import FWCore.ParameterSet.Config as cms

def PATSecondaryVertexSlimmer(**kwargs):
  mod = cms.EDProducer('PATSecondaryVertexSlimmer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
