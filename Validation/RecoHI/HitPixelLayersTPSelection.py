import FWCore.ParameterSet.Config as cms

def HitPixelLayersTPSelection(*args, **kwargs):
  mod = cms.EDFilter('HitPixelLayersTPSelection',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
