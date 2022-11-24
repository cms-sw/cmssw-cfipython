import FWCore.ParameterSet.Config as cms

testonelumifilllumi = cms.EDProducer('TestDQMOneLumiFillLumiEDAnalyzer',
  folder = cms.string('One/testonelumifilllumi'),
  howmany = cms.int32(1),
  value = cms.double(1),
  mightGet = cms.optional.untracked.vstring
)
