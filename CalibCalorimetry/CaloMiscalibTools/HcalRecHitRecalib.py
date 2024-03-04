import FWCore.ParameterSet.Config as cms

def HcalRecHitRecalib(**kwargs):
  mod = cms.EDProducer('HcalRecHitRecalib',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
