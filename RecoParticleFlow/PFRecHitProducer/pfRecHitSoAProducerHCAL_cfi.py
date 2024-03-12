import FWCore.ParameterSet.Config as cms

pfRecHitSoAProducerHCAL = cms.EDProducer('PFRecHitSoAProducerHCAL@alpaka',
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
