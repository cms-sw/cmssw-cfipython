import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncCAHitNtupletAlpakaPhase2 = cms.EDProducer('alpaka_rocm_async::CAHitNtupletAlpakaPhase2',
  pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingAlpaka'),
  CPE = cms.string('PixelCPEFastParamsPhase2'),
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
  maxNumberOfDoublets = cms.uint32(2621440),
  idealConditions = cms.bool(False),
  includeFarForwards = cms.bool(True),
  includeJumpingForwardDoublets = cms.bool(True),
  cellZ0Cut = cms.double(7.5),
  cellPtCut = cms.double(0.85),
  trackQualityCuts = cms.PSet(
    maxChi2 = cms.double(5),
    minPt = cms.double(0.5),
    maxTip = cms.double(0.3),
    maxZip = cms.double(12)
  ),
  phiCuts = cms.vint32(
    522,
    522,
    522,
    626,
    730,
    730,
    626,
    730,
    730,
    522,
    522,
    522,
    522,
    522,
    522,
    522,
    522,
    522,
    522,
    522,
    522,
    522,
    522,
    522,
    522,
    522,
    522,
    522,
    522,
    730,
    730,
    730,
    730,
    730,
    730,
    730,
    730,
    730,
    730,
    730,
    730,
    730,
    730,
    730,
    730,
    730,
    730,
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