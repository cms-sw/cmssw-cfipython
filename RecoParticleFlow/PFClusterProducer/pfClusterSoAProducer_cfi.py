import FWCore.ParameterSet.Config as cms

pfClusterSoAProducer = cms.EDProducer('PFClusterSoAProducer@alpaka',
  pfRecHits = cms.required.InputTag,
  pfClusterParams = cms.required.ESInputTag,
  synchronise = cms.required.bool,
  pfRecHitFractionAllocation = cms.int32(120),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
