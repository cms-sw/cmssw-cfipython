import FWCore.ParameterSet.Config as cms

def TotemTimingLocalTrackFitter_CTPPSDiamondDetId_(**kwargs):
  mod = cms.EDProducer('TotemTimingLocalTrackFitter<CTPPSDiamondDetId>',
    recHitsTag = cms.InputTag('totemTimingRecHits'),
    maxPlaneActiveChannels = cms.int32(2),
    trackingAlgorithmParams = cms.PSet(
      threshold = cms.double(1.5),
      thresholdFromMaximum = cms.double(0.5),
      resolution = cms.double(0.01),
      sigma = cms.double(0),
      tolerance = cms.double(0.1),
      pixelEfficiencyFunction = cms.string('(x>[0]-0.5*[1]-0.05)*(x<[0]+0.5*[1]-0.05)+0*[2]'),
      yPosition = cms.double(0),
      yWidth = cms.double(0)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
