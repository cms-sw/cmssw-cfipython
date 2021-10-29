import FWCore.ParameterSet.Config as cms

btlSimHitsPostProcessor = cms.EDProducer('BtlSimHitsHarvester',
  folder = cms.string('MTD/BTL/SimHits/'),
  mightGet = cms.optional.untracked.vstring
)
