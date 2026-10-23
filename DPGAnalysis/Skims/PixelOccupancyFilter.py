import FWCore.ParameterSet.Config as cms

def PixelOccupancyFilter(*args, **kwargs):
  mod = cms.EDFilter('PixelOccupancyFilter',
    src = cms.InputTag(''),
    minDetSetCounts = cms.uint32(0),
    maxDetSetCounts = cms.uint32(0),
    minNumber = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
