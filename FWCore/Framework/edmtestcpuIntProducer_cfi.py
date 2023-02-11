import FWCore.ParameterSet.Config as cms

edmtestcpuIntProducer = cms.EDProducer('edm::test::cpu::IntProducer',
  valueOther = cms.required.int32,
  valueCpu = cms.required.int32,
  variant = cms.untracked.string(''),
  mightGet = cms.optional.untracked.vstring
)
