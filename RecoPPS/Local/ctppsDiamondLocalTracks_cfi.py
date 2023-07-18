import FWCore.ParameterSet.Config as cms

ctppsDiamondLocalTracks = cms.EDProducer('CTPPSDiamondLocalTrackFitter',
  recHitsTag = cms.InputTag('ctppsDiamondRecHits'),
  trackingAlgorithmParams = cms.PSet(
    threshold = cms.double(1.5),
    thresholdFromMaximum = cms.double(0.5),
    resolution = cms.double(0.01),
    sigma = cms.double(0.1),
    startFromX = cms.double(-0.5),
    stopAtX = cms.double(19.5),
    tolerance = cms.double(0.1),
    pixelEfficiencyFunction = cms.string('(x>[0]-0.5*[1])*(x<[0]+0.5*[1])+0*[2]'),
    yPosition = cms.double(0),
    yWidth = cms.double(0),
    excludeSingleEdgeHits = cms.bool(True)
  ),
  mightGet = cms.optional.untracked.vstring
)
