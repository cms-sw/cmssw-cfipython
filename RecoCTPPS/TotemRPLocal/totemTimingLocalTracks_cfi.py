import FWCore.ParameterSet.Config as cms

totemTimingLocalTracks = cms.EDProducer('TotemTimingLocalTrackFitter',
  recHitsTag = cms.InputTag('totemTimingRecHits'),
  verbosity = cms.int32(0),
  threshold = cms.double(1.5),
  thresholdFromMaximum = cms.double(0.5),
  resolution = cms.double(0.01),
  sigma = cms.double(0),
  tolerance = cms.double(0.1),
  maxPlaneActiveChannels = cms.int32(2),
  pixelEfficiencyFunction = cms.string('(x>[0]-0.5*[1]-0.05)*(x<[0]+0.5*[1]-0.05)+0*[2]'),
  yPosition = cms.double(0),
  yWidth = cms.double(0)
)
