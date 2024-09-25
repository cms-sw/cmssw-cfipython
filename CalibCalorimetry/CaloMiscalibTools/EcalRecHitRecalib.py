import FWCore.ParameterSet.Config as cms

def EcalRecHitRecalib(*args, **kwargs):
  mod = cms.EDProducer('EcalRecHitRecalib',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
