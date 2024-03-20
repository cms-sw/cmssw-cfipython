import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncTestAlpakaProducer = cms.EDProducer('alpaka_rocm_async::TestAlpakaProducer',
  size = cms.required.int32,
  size2 = cms.required.int32,
  size3 = cms.required.int32,
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
