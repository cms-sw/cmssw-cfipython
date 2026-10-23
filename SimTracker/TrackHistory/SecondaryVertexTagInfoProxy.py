import FWCore.ParameterSet.Config as cms

def SecondaryVertexTagInfoProxy(*args, **kwargs):
  mod = cms.EDProducer('SecondaryVertexTagInfoProxy',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
