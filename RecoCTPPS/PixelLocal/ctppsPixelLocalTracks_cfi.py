import FWCore.ParameterSet.Config as cms

ctppsPixelLocalTracks = cms.EDProducer('CTPPSPixelLocalTrackProducer',
  label = cms.string('ctppsPixelRecHits'),
  patternFinderAlgorithm = cms.string('RPixRoadFinder'),
  trackFinderAlgorithm = cms.string('RPixPlaneCombinatoryTracking'),
  trackMinNumberOfPoints = cms.uint32(3),
  verbosity = cms.untracked.int32(0),
  maximumChi2OverNDF = cms.double(5),
  maximumXLocalDistanceFromTrack = cms.double(0.2),
  maximumYLocalDistanceFromTrack = cms.double(0.3),
  maxHitPerPlane = cms.int32(20),
  maxHitPerRomanPot = cms.int32(60),
  maxTrackPerRomanPot = cms.int32(10),
  maxTrackPerPattern = cms.int32(5),
  numberOfPlanesPerPot = cms.int32(6),
  roadRadius = cms.double(1),
  minRoadSize = cms.int32(3),
  maxRoadSize = cms.int32(20)
)
