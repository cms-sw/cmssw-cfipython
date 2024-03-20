import FWCore.ParameterSet.Config as cms

alpaka_serial_syncAlpakaBackendProducer = cms.EDProducer('alpaka_serial_sync::AlpakaBackendProducer',
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
