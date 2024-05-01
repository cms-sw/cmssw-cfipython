import FWCore.ParameterSet.Config as cms

testAlpakaGlobalProducerNoOutput = cms.EDProducer('TestAlpakaGlobalProducerNoOutput@alpaka',
  source = cms.InputTag(''),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
