import FWCore.ParameterSet.Config as cms

testAlpakaGlobalProducerNullES = cms.EDProducer('TestAlpakaGlobalProducerNullES@alpaka',
  eventSetupSource = cms.ESInputTag('', ''),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
