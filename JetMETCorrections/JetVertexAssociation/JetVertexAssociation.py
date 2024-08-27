import FWCore.ParameterSet.Config as cms

def JetVertexAssociation(**kwargs):
  mod = cms.EDProducer('JetVertexAssociation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
