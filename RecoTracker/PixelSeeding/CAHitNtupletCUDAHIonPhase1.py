import FWCore.ParameterSet.Config as cms

def CAHitNtupletCUDAHIonPhase1(**kwargs):
  mod = cms.EDProducer('CAHitNtupletCUDAHIonPhase1',
    onGPU = cms.bool(True),
    pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingCUDA'),
    ptmin = cms.double(0.9),
    CAThetaCutBarrel = cms.double(0.002),
    CAThetaCutForward = cms.double(0.003),
    hardCurvCut = cms.double(0.032840722495894911),
    dcaCutInnerTriplet = cms.double(0.15),
    dcaCutOuterTriplet = cms.double(0.25),
    earlyFishbone = cms.bool(True),
    lateFishbone = cms.bool(False),
    fillStatistics = cms.bool(False),
    minHitsPerNtuplet = cms.uint32(4),
    maxNumberOfDoublets = cms.uint32(3145728),
    minHitsForSharingCut = cms.uint32(10),
    fitNas4 = cms.bool(False),
    doClusterCut = cms.bool(True),
    doZ0Cut = cms.bool(True),
    doPtCut = cms.bool(True),
    useRiemannFit = cms.bool(False),
    doSharedHitCut = cms.bool(True),
    dupPassThrough = cms.bool(False),
    useSimpleTripletCleaner = cms.bool(True),
    idealConditions = cms.bool(False),
    includeJumpingForwardDoublets = cms.bool(False),
    z0Cut = cms.double(10),
    ptCut = cms.double(0),
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
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
