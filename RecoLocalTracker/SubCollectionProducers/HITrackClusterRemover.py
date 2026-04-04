import FWCore.ParameterSet.Config as cms

def HITrackClusterRemover(*args, **kwargs):
  mod = cms.EDProducer('HITrackClusterRemover',
    Common = cms.PSet(
      maxChi2 = cms.optional.double,
      maxCharge = cms.double(0),
      minGoodPixelCharge = cms.double(0),
      minGoodStripCharge = cms.double(0),
      maxSize = cms.uint32(0)
    ),
    Pixel = cms.PSet(
      maxChi2 = cms.optional.double,
      maxCharge = cms.double(0),
      minGoodPixelCharge = cms.double(0),
      minGoodStripCharge = cms.double(0),
      maxSize = cms.uint32(0)
    ),
    Strip = cms.PSet(
      maxChi2 = cms.optional.double,
      maxCharge = cms.double(0),
      minGoodPixelCharge = cms.double(0),
      minGoodStripCharge = cms.double(0),
      maxSize = cms.uint32(0)
    ),
    PXB = cms.PSet(
      maxChi2 = cms.optional.double,
      maxCharge = cms.double(0),
      minGoodPixelCharge = cms.double(0),
      minGoodStripCharge = cms.double(0),
      maxSize = cms.uint32(0)
    ),
    PXE = cms.PSet(
      maxChi2 = cms.optional.double,
      maxCharge = cms.double(0),
      minGoodPixelCharge = cms.double(0),
      minGoodStripCharge = cms.double(0),
      maxSize = cms.uint32(0)
    ),
    StripInner = cms.PSet(
      maxChi2 = cms.optional.double,
      maxCharge = cms.double(0),
      minGoodPixelCharge = cms.double(0),
      minGoodStripCharge = cms.double(0),
      maxSize = cms.uint32(0)
    ),
    StripOuter = cms.PSet(
      maxChi2 = cms.optional.double,
      maxCharge = cms.double(0),
      minGoodPixelCharge = cms.double(0),
      minGoodStripCharge = cms.double(0),
      maxSize = cms.uint32(0)
    ),
    TIB = cms.PSet(
      maxChi2 = cms.optional.double,
      maxCharge = cms.double(0),
      minGoodPixelCharge = cms.double(0),
      minGoodStripCharge = cms.double(0),
      maxSize = cms.uint32(0)
    ),
    TID = cms.PSet(
      maxChi2 = cms.optional.double,
      maxCharge = cms.double(0),
      minGoodPixelCharge = cms.double(0),
      minGoodStripCharge = cms.double(0),
      maxSize = cms.uint32(0)
    ),
    TOB = cms.PSet(
      maxChi2 = cms.optional.double,
      maxCharge = cms.double(0),
      minGoodPixelCharge = cms.double(0),
      minGoodStripCharge = cms.double(0),
      maxSize = cms.uint32(0)
    ),
    TEC = cms.PSet(
      maxChi2 = cms.optional.double,
      maxCharge = cms.double(0),
      minGoodPixelCharge = cms.double(0),
      minGoodStripCharge = cms.double(0),
      maxSize = cms.uint32(0)
    ),
    doStrip = cms.bool(True),
    doPixel = cms.bool(True),
    doStripChargeCheck = cms.bool(False),
    doPixelChargeCheck = cms.bool(False),
    stripRecHits = cms.required.string,
    pixelRecHits = cms.required.string,
    oldClusterRemovalInfo = cms.InputTag(''),
    overrideTrkQuals = cms.InputTag(''),
    clusterLessSolution = cms.bool(False),
    TrackQuality = cms.string(''),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    trajectories = cms.InputTag(''),
    pixelClusters = cms.required.InputTag,
    stripClusters = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
