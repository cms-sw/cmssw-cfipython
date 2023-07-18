import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncTestAlpakaProducer = cms.EDProducer('alpaka_cuda_async::TestAlpakaProducer',
  size = cms.required.int32,
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
