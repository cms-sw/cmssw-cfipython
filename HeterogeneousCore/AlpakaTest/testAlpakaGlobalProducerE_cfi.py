import FWCore.ParameterSet.Config as cms

testAlpakaGlobalProducerE = cms.EDProducer('TestAlpakaGlobalProducerE@alpaka',
  eventSetupSource = cms.ESInputTag('', ''),
  source = cms.InputTag(''),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
