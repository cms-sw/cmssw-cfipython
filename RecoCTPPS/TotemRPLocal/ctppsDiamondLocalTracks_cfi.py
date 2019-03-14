import FWCore.ParameterSet.Config as cms

ctppsDiamondLocalTracks = cms.EDProducer('CTPPSDiamondLocalTrackFitter',
  recHitsTag = cms.InputTag('ctppsDiamondRecHits'),
  verbosity = cms.int32(0),
  trackingAlgorithmParams = cms.PSet(
    threshold = cms.double(1.5),
    thresholdFromMaximum = cms.double(0.5),
    resolution = cms.double(0.01),
    sigma = cms.double(0.1),
    startFromX = cms.double(-0.5),
    stopAtX = cms.double(19.5),
    pixelEfficiencyFunction = cms.string('(TMath::Erf((x-[0]+0.5*[1])/([2]/4)+2)+1)*TMath::Erfc((x-[0]-0.5*[1])/([2]/4)-2)/4'),
    yPosition = cms.double(0),
    yWidth = cms.double(0)
  )
)
