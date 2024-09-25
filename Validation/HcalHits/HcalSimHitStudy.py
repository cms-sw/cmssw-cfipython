import FWCore.ParameterSet.Config as cms

def HcalSimHitStudy(*args, **kwargs):
  mod = cms.EDProducer('HcalSimHitStudy',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
