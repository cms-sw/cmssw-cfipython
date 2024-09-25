import FWCore.ParameterSet.Config as cms

def CAHitNtupletAlpakaPhase1_alpaka(*args, **kwargs):
  mod = cms.EDProducer('CAHitNtupletAlpakaPhase1@alpaka',
    pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingAlpaka'),
    CPE = cms.string('PixelCPEFastParams'),
    ptmin = cms.double(0.89999997615814209),
    CAThetaCutBarrel = cms.double(0.0020000000949949026),
    CAThetaCutForward = cms.double(0.0030000000260770321),
    hardCurvCut = cms.double(0.032840722495894911),
    dcaCutInnerTriplet = cms.double(0.15000000596046448),
    dcaCutOuterTriplet = cms.double(0.25),
    earlyFishbone = cms.bool(True),
    lateFishbone = cms.bool(False),
    fillStatistics = cms.bool(False),
    minHitsPerNtuplet = cms.uint32(4),
    minHitsForSharingCut = cms.uint32(10),
    fitNas4 = cms.bool(False),
    doClusterCut = cms.bool(True),
    doZ0Cut = cms.bool(True),
    doPtCut = cms.bool(True),
    useRiemannFit = cms.bool(False),
    doSharedHitCut = cms.bool(True),
    dupPassThrough = cms.bool(False),
    useSimpleTripletCleaner = cms.bool(True),
    maxNumberOfDoublets = cms.uint32(524288),
    idealConditions = cms.bool(True),
    includeJumpingForwardDoublets = cms.bool(False),
    cellZ0Cut = cms.double(12),
    cellPtCut = cms.double(0.5),
    trackQualityCuts = cms.PSet(
      chi2MaxPt = cms.double(10),
      chi2Coeff = cms.vdouble(
        0.9,
        1.8
      ),
      chi2Scale = cms.double(8),
      tripletMinPt = cms.double(0.5),
      tripletMaxTip = cms.double(0.3),
      tripletMaxZip = cms.double(12),
      quadrupletMinPt = cms.double(0.3),
      quadrupletMaxTip = cms.double(0.5),
      quadrupletMaxZip = cms.double(12)
    ),
    phiCuts = cms.vint32(
      522,
      730,
      730,
      522,
      626,
      626,
      522,
      522,
      626,
      626,
      626,
      522,
      522,
      522,
      522,
      522,
      522,
      522,
      522
    ),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
