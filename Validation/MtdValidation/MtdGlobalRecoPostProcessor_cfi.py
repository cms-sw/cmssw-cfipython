import FWCore.ParameterSet.Config as cms

MtdGlobalRecoPostProcessor = cms.EDProducer('MtdGlobalRecoHarvester',
  folder = cms.string('MTD/GlobalReco/'),
  mightGet = cms.optional.untracked.vstring
)
