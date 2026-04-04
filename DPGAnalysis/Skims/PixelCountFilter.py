import FWCore.ParameterSet.Config as cms

def PixelCountFilter(*args, **kwargs):
  mod = cms.EDFilter('PixelCountFilter',
    src = cms.InputTag(''),
    minNumber = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
