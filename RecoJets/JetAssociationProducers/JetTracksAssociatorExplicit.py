import FWCore.ParameterSet.Config as cms

def JetTracksAssociatorExplicit(*args, **kwargs):
  mod = cms.EDProducer('JetTracksAssociatorExplicit',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
