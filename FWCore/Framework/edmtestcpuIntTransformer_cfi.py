import FWCore.ParameterSet.Config as cms

edmtestcpuIntTransformer = cms.EDProducer('edm::test::cpu::IntTransformer',
  valueOther = cms.required.int32,
  valueCpu = cms.required.int32,
  variant = cms.untracked.string(''),
  mightGet = cms.optional.untracked.vstring
)
