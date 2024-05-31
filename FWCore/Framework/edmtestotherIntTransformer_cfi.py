import FWCore.ParameterSet.Config as cms

edmtestotherIntTransformer = cms.EDProducer('edm::test::other::IntTransformer',
  valueOther = cms.required.int32,
  valueCpu = cms.required.int32,
  variant = cms.untracked.string(''),
  mightGet = cms.optional.untracked.vstring
)
