import FWCore.ParameterSet.Config as cms

alpaka_serial_syncHCALRecHitSoAProducer = cms.EDProducer('alpaka_serial_sync::HCALRecHitSoAProducer',
  src = cms.required.InputTag,
  synchronise = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
