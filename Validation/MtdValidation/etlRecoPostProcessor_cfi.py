import FWCore.ParameterSet.Config as cms

etlRecoPostProcessor = cms.EDProducer('EtlRecoHarvester',
  folder = cms.string('MTD/ETL/Reco/'),
  mightGet = cms.optional.untracked.vstring
)
