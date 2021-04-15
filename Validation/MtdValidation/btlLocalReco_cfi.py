import FWCore.ParameterSet.Config as cms

btlLocalReco = cms.EDProducer('BtlLocalRecoValidation',
  folder = cms.string('MTD/BTL/LocalReco'),
  recHitsTag = cms.InputTag('mtdRecHits', 'FTLBarrel'),
  simHitsTag = cms.InputTag('mix', 'g4SimHitsFastTimerHitsBarrel'),
  recCluTag = cms.InputTag('mtdClusters', 'FTLBarrel'),
  hitMinimumEnergy = cms.double(1),
  LocalPositionDebug = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
