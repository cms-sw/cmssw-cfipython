import FWCore.ParameterSet.Config as cms

def PixelOccupancyFilter(**kwargs):
  mod = cms.EDFilter('PixelOccupancyFilter',
    src = cms.InputTag(''),
    minDetSetCounts = cms.uint32(0),
    maxDetSetCounts = cms.uint32(0),
    minNumber = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
