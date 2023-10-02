import FWCore.ParameterSet.Config as cms

pixelOccupancyFilter = cms.EDFilter('PixelOccupancyFilter',
  src = cms.InputTag(''),
  minDetSetCounts = cms.uint32(0),
  maxDetSetCounts = cms.uint32(0),
  minNumber = cms.uint32(0),
  mightGet = cms.optional.untracked.vstring
)
