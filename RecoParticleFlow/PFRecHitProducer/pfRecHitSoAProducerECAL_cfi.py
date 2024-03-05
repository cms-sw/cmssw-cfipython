import FWCore.ParameterSet.Config as cms

pfRecHitSoAProducerECAL = cms.EDProducer('PFRecHitSoAProducerECAL@alpaka',
  producers = cms.VPSet(
    cms.PSet(
      src = cms.InputTag('')
    )
  ),
  topology = cms.ESInputTag('', ''),
  synchronise = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
