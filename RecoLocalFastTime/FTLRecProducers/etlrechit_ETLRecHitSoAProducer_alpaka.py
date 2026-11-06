import FWCore.ParameterSet.Config as cms

def etlrechit_ETLRecHitSoAProducer_alpaka(*args, **kwargs):
  mod = cms.EDProducer('etlrechit::ETLRecHitSoAProducer@alpaka',
    baserh = cms.required.InputTag,
    thresholdToKeep = cms.required.double,
    timeResInNs = cms.required.double,
    timeCorr_p0 = cms.required.double,
    timeCorr_p1 = cms.required.double,
    timeCorr_p2 = cms.required.double,
    timeCorr_p3 = cms.required.double,
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
