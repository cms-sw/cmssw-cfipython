import FWCore.ParameterSet.Config as cms

def JetVertexAssociation(*args, **kwargs):
  mod = cms.EDProducer('JetVertexAssociation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
