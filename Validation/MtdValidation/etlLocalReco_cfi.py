import FWCore.ParameterSet.Config as cms

etlLocalReco = cms.EDProducer('EtlLocalRecoValidation',
  folder = cms.string('MTD/ETL/LocalReco'),
  recHitsTag = cms.InputTag('mtdRecHits', 'FTLEndcap'),
  recCluTag = cms.InputTag('mtdClusters', 'FTLEndcap'),
  hitMinimumEnergy = cms.double(1),
  mightGet = cms.optional.untracked.vstring
)
