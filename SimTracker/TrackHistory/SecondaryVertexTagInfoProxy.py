import FWCore.ParameterSet.Config as cms

def SecondaryVertexTagInfoProxy(**kwargs):
  mod = cms.EDProducer('SecondaryVertexTagInfoProxy',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
