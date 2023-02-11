import FWCore.ParameterSet.Config as cms

edmtestotherIntProducer = cms.EDProducer('edm::test::other::IntProducer',
  valueOther = cms.required.int32,
  valueCpu = cms.required.int32,
  variant = cms.untracked.string(''),
  mightGet = cms.optional.untracked.vstring
)
