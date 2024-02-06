import FWCore.ParameterSet.Config as cms

alpaka_serial_syncECALRecHitSoAProducer = cms.EDProducer('alpaka_serial_sync::ECALRecHitSoAProducer',
  src = cms.required.InputTag,
  synchronise = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
