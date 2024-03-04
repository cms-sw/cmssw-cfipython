import FWCore.ParameterSet.Config as cms

def HcalSimHitStudy(**kwargs):
  mod = cms.EDProducer('HcalSimHitStudy',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
