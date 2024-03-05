import FWCore.ParameterSet.Config as cms

alpaka_serial_syncPFClusterSoAProducer = cms.EDProducer('alpaka_serial_sync::PFClusterSoAProducer',
  pfRecHits = cms.InputTag(''),
  pfClusterParams = cms.ESInputTag('', ''),
  topology = cms.ESInputTag('', ''),
  synchronise = cms.bool(False),
  pfRecHitFractionAllocation = cms.int32(120),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
