import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_ECALRecHitSoAProducer(**kwargs):
  mod = cms.EDProducer('alpaka_serial_sync::ECALRecHitSoAProducer',
    src = cms.InputTag(''),
    synchronise = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod