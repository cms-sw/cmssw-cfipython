import FWCore.ParameterSet.Config as cms

btlLocalRecoPostProcessor = cms.EDProducer('BtlLocalRecoHarvester',
  folder = cms.string('MTD/BTL/LocalReco/'),
  mightGet = cms.optional.untracked.vstring
)
