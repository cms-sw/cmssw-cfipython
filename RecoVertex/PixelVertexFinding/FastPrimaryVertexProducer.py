import FWCore.ParameterSet.Config as cms

def FastPrimaryVertexProducer(*args, **kwargs):
  mod = cms.EDProducer('FastPrimaryVertexProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
