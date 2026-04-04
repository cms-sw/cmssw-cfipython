import FWCore.ParameterSet.Config as cms

def CrossingFramePSimHitToPSimHitsConverter(*args, **kwargs):
  mod = cms.EDProducer('CrossingFramePSimHitToPSimHitsConverter',
    src = cms.VInputTag(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
