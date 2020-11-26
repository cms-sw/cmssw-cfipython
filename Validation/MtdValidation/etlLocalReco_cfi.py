import FWCore.ParameterSet.Config as cms

etlLocalReco = cms.EDProducer('EtlLocalRecoValidation',
  folder = cms.string('MTD/ETL/LocalReco'),
  recHitsTag = cms.InputTag('mtdRecHits', 'FTLEndcap'),
  recCluTag = cms.InputTag('mtdClusters', 'FTLEndcap'),
  hitMinimumEnergy1Dis = cms.double(1),
  hitMinimumEnergy2Dis = cms.double(0.001),
  mightGet = cms.optional.untracked.vstring
)
