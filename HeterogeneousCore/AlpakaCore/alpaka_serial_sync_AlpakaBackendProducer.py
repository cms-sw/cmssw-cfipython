import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_AlpakaBackendProducer(**kwargs):
  mod = cms.EDProducer('alpaka_serial_sync::AlpakaBackendProducer',
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
