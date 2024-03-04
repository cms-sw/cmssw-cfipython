import FWCore.ParameterSet.Config as cms

def CrossingFramePSimHitToPSimHitsConverter(**kwargs):
  mod = cms.EDProducer('CrossingFramePSimHitToPSimHitsConverter',
    src = cms.VInputTag(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
