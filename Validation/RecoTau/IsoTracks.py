import FWCore.ParameterSet.Config as cms

def IsoTracks(*args, **kwargs):
  mod = cms.EDProducer('IsoTracks',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
