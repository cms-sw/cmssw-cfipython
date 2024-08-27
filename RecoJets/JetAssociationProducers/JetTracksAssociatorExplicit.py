import FWCore.ParameterSet.Config as cms

def JetTracksAssociatorExplicit(**kwargs):
  mod = cms.EDProducer('JetTracksAssociatorExplicit',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
