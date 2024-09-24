import FWCore.ParameterSet.Config as cms

def TrackerTrackHitFilter(*args, **kwargs):
  mod = cms.EDProducer('TrackerTrackHitFilter',
    src = cms.InputTag('generalTracks'),
    minimumHits = cms.uint32(3),
    replaceWithInactiveHits = cms.bool(False),
    truncateTracks = cms.bool(False),
    layersRemaining = cms.uint32(8),
    stripFrontInvalidHits = cms.bool(False),
    stripBackInvalidHits = cms.bool(False),
    stripAllInvalidHits = cms.bool(False),
    isPhase2 = cms.bool(False),
    rejectBadStoNHits = cms.bool(False),
    CMNSubtractionMode = cms.string('Median'),
    detsToIgnore = cms.vuint32(),
    useTrajectories = cms.bool(False),
    rejectLowAngleHits = cms.bool(False),
    TrackAngleCut = cms.double(0.25),
    usePixelQualityFlag = cms.bool(False),
    PxlTemplateProbXYCut = cms.double(0.000125),
    PxlTemplateProbXYChargeCut = cms.double(-99),
    PxlTemplateqBinCut = cms.vint32(
      0,
      3
    ),
    PxlCorrClusterChargeCut = cms.double(-999),
    tagOverlaps = cms.bool(False),
    commands = cms.vstring(),
    StoNcommands = cms.vstring(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
