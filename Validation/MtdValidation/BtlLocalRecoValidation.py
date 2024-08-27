import FWCore.ParameterSet.Config as cms

def BtlLocalRecoValidation(**kwargs):
  mod = cms.EDProducer('BtlLocalRecoValidation',
    folder = cms.string('MTD/BTL/LocalReco'),
    recHitsTag = cms.InputTag('mtdRecHits', 'FTLBarrel'),
    uncalibRecHitsTag = cms.InputTag('mtdUncalibratedRecHits', 'FTLBarrel'),
    simHitsTag = cms.InputTag('mix', 'g4SimHitsFastTimerHitsBarrel'),
    recCluTag = cms.InputTag('mtdClusters', 'FTLBarrel'),
    trkHitTag = cms.InputTag('mtdTrackingRecHits'),
    r2sAssociationMapTag = cms.InputTag('mtdRecoClusterToSimLayerClusterAssociation'),
    HitMinimumEnergy = cms.double(1),
    optionalPlots = cms.bool(False),
    UncalibRecHitsPlots = cms.bool(False),
    HitMinimumAmplitude = cms.double(30),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
