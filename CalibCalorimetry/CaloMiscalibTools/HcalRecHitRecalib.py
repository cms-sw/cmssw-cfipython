import FWCore.ParameterSet.Config as cms

def HcalRecHitRecalib(*args, **kwargs):
  mod = cms.EDProducer('HcalRecHitRecalib',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
