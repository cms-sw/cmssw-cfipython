import FWCore.ParameterSet.Config as cms

def HiEvtPlaneFlatProducer(*args, **kwargs):
  mod = cms.EDProducer('HiEvtPlaneFlatProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
