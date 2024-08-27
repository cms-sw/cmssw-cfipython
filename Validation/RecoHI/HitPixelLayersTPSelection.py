import FWCore.ParameterSet.Config as cms

def HitPixelLayersTPSelection(**kwargs):
  mod = cms.EDFilter('HitPixelLayersTPSelection',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
