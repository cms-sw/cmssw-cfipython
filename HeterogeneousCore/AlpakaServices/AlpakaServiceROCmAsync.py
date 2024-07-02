import FWCore.ParameterSet.Config as cms

def AlpakaServiceROCmAsync(**kwargs):
  mod = cms.Service('AlpakaServiceROCmAsync',
    enabled = cms.untracked.bool(True),
    verbose = cms.untracked.bool(False),
    hostAllocator = cms.untracked.PSet(
      binGrowth = cms.untracked.uint32(2),
      minBin = cms.untracked.uint32(8),
      maxBin = cms.untracked.uint32(30),
      maxCachedBytes = cms.untracked.uint64(0),
      maxCachedFraction = cms.untracked.double(0.8),
      fillAllocations = cms.untracked.bool(False),
      fillAllocationValue = cms.untracked.uint32(165),
      fillReallocations = cms.untracked.bool(False),
      fillReallocationValue = cms.untracked.uint32(105),
      fillDeallocations = cms.untracked.bool(False),
      fillDeallocationValue = cms.untracked.uint32(90),
      fillCaches = cms.untracked.bool(False),
      fillCacheValue = cms.untracked.uint32(150)
    ),
    deviceAllocator = cms.untracked.PSet(
      binGrowth = cms.untracked.uint32(2),
      minBin = cms.untracked.uint32(8),
      maxBin = cms.untracked.uint32(30),
      maxCachedBytes = cms.untracked.uint64(0),
      maxCachedFraction = cms.untracked.double(0.8),
      fillAllocations = cms.untracked.bool(False),
      fillAllocationValue = cms.untracked.uint32(165),
      fillReallocations = cms.untracked.bool(False),
      fillReallocationValue = cms.untracked.uint32(105),
      fillDeallocations = cms.untracked.bool(False),
      fillDeallocationValue = cms.untracked.uint32(90),
      fillCaches = cms.untracked.bool(False),
      fillCacheValue = cms.untracked.uint32(150)
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
