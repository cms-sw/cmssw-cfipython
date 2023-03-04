import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncTestAlpakaStreamSynchronizingProducer = cms.EDProducer('alpaka_rocm_async::TestAlpakaStreamSynchronizingProducer',
  source = cms.required.InputTag,
  intSource = cms.required.InputTag,
  expectedInt = cms.required.int32,
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
