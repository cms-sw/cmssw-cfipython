import FWCore.ParameterSet.Config as cms

etlLocalRecoValid = cms.EDProducer('EtlLocalRecoValidation',
  folder = cms.string('MTD/ETL/LocalReco'),
  recHitsTag = cms.InputTag('mtdRecHits', 'FTLEndcap'),
  uncalibRecHitsTag = cms.InputTag('mtdUncalibratedRecHits', 'FTLEndcap'),
  simHitsTag = cms.InputTag('mix', 'g4SimHitsFastTimerHitsEndcap'),
  recCluTag = cms.InputTag('mtdClusters', 'FTLEndcap'),
  trkHitTag = cms.InputTag('mtdTrackingRecHits'),
  hitMinimumEnergy2Dis = cms.double(0.001),
  optionalPlots = cms.bool(False),
  UncalibRecHitsPlots = cms.bool(False),
  HitMinimumAmplitude = cms.double(0.33),
  mightGet = cms.optional.untracked.vstring
)
