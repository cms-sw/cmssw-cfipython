import FWCore.ParameterSet.Config as cms

def HGCalRecHitsProducer_alpaka(*args, **kwargs):
  mod = cms.EDProducer('HGCalRecHitsProducer@alpaka',
    digis = cms.InputTag('hgcalDigis', 'DIGI', 'TEST'),
    calibSource = cms.ESInputTag('', ''),
    configSource = cms.ESInputTag('', ''),
    n_blocks = cms.int32(-1),
    n_threads = cms.int32(-1),
    n_hits_scale = cms.int32(-1),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string(''),
      synchronize = cms.optional.untracked.bool
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
