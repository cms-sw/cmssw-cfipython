import FWCore.ParameterSet.Config as cms

def JetTracksAssociatorAtCaloFace(*args, **kwargs):
  mod = cms.EDProducer('JetTracksAssociatorAtCaloFace',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
