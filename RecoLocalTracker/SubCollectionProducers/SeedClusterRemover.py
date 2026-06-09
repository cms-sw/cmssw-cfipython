import FWCore.ParameterSet.Config as cms

def SeedClusterRemover(*args, **kwargs):
  mod = cms.EDProducer('SeedClusterRemover',
    Common = cms.PSet(
      maxChi2 = cms.optional.double,
      maxCharge = cms.double(0),
      maxSize = cms.uint32(0)
    ),
    Pixel = cms.PSet(
      maxChi2 = cms.optional.double,
      maxCharge = cms.double(0),
      maxSize = cms.uint32(0)
    ),
    Strip = cms.PSet(
      maxChi2 = cms.optional.double,
      maxCharge = cms.double(0),
      maxSize = cms.uint32(0)
    ),
    PXB = cms.PSet(
      maxChi2 = cms.optional.double,
      maxCharge = cms.double(0),
      maxSize = cms.uint32(0)
    ),
    PXE = cms.PSet(
      maxChi2 = cms.optional.double,
      maxCharge = cms.double(0),
      maxSize = cms.uint32(0)
    ),
    StripInner = cms.PSet(
      maxChi2 = cms.optional.double,
      maxCharge = cms.double(0),
      maxSize = cms.uint32(0)
    ),
    StripOuter = cms.PSet(
      maxChi2 = cms.optional.double,
      maxCharge = cms.double(0),
      maxSize = cms.uint32(0)
    ),
    TIB = cms.PSet(
      maxChi2 = cms.optional.double,
      maxCharge = cms.double(0),
      maxSize = cms.uint32(0)
    ),
    TID = cms.PSet(
      maxChi2 = cms.optional.double,
      maxCharge = cms.double(0),
      maxSize = cms.uint32(0)
    ),
    TOB = cms.PSet(
      maxChi2 = cms.optional.double,
      maxCharge = cms.double(0),
      maxSize = cms.uint32(0)
    ),
    TEC = cms.PSet(
      maxChi2 = cms.optional.double,
      maxCharge = cms.double(0),
      maxSize = cms.uint32(0)
    ),
    doStrip = cms.bool(True),
    doPixel = cms.bool(True),
    trajectories = cms.required.InputTag,
    pixelClusters = cms.required.InputTag,
    stripClusters = cms.required.InputTag,
    oldClusterRemovalInfo = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
