import FWCore.ParameterSet.Config as cms

testAlpakaStreamSynchronizingProducer = cms.EDProducer('TestAlpakaStreamSynchronizingProducer@alpaka',
  source = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
