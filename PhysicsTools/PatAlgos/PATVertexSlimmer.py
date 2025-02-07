import FWCore.ParameterSet.Config as cms

def PATVertexSlimmer(*args, **kwargs):
  mod = cms.EDProducer('PATVertexSlimmer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
