import FWCore.ParameterSet.Config as cms

def PATSecondaryVertexSlimmer(*args, **kwargs):
  mod = cms.EDProducer('PATSecondaryVertexSlimmer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
