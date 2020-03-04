import FWCore.ParameterSet.Config as cms

btlRecoPostProcessor = cms.EDProducer('BtlRecoHarvester',
  folder = cms.string('MTD/BTL/Reco/'),
  mightGet = cms.optional.untracked.vstring
)
