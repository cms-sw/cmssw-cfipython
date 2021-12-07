import FWCore.ParameterSet.Config as cms

btlLocalReco = cms.EDProducer('BtlLocalRecoValidation',
  folder = cms.string('MTD/BTL/LocalReco'),
  recHitsTag = cms.InputTag('mtdRecHits', 'FTLBarrel'),
  uncalibRecHitsTag = cms.InputTag('mtdUncalibratedRecHits', 'FTLBarrel'),
  simHitsTag = cms.InputTag('mix', 'g4SimHitsFastTimerHitsBarrel'),
  recCluTag = cms.InputTag('mtdClusters', 'FTLBarrel'),
  HitMinimumEnergy = cms.double(1),
  LocalPositionDebug = cms.bool(False),
  UncalibRecHitsPlots = cms.bool(False),
  HitMinimumAmplitude = cms.double(30),
  mightGet = cms.optional.untracked.vstring
)
