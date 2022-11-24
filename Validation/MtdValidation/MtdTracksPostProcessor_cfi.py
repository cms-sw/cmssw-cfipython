import FWCore.ParameterSet.Config as cms

MtdTracksPostProcessor = cms.EDProducer('MtdTracksHarvester',
  folder = cms.string('MTD/Tracks/'),
  mightGet = cms.optional.untracked.vstring
)
