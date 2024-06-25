import FWCore.ParameterSet.Config as cms

def CAHitNtupletAlpakaHIonPhase1_alpaka(**kwargs):
  mod = cms.EDProducer('CAHitNtupletAlpakaHIonPhase1@alpaka',
    pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingAlpaka'),
    CPE = cms.string('PixelCPEFastParamsHIonPhase1'),
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
    maxNumberOfDoublets = cms.uint32(3145728),
    idealConditions = cms.bool(False),
    includeJumpingForwardDoublets = cms.bool(False),
    cellZ0Cut = cms.double(10),
    cellPtCut = cms.double(0),
    trackQualityCuts = cms.PSet(
      chi2MaxPt = cms.double(10),
      chi2Coeff = cms.vdouble(
        0.9,
        1.8
      ),
      chi2Scale = cms.double(8),
      tripletMinPt = cms.double(0),
      tripletMaxTip = cms.double(0.1),
      tripletMaxZip = cms.double(6),
      quadrupletMinPt = cms.double(0),
      quadrupletMaxTip = cms.double(0.5),
      quadrupletMaxZip = cms.double(6)
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
