import FWCore.ParameterSet.Config as cms

testharvester = cms.EDProducer('TestHarvester',
  folder = cms.string('Harvesting/'),
  mightGet = cms.optional.untracked.vstring
)
