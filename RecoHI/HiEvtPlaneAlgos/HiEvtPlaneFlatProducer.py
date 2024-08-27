import FWCore.ParameterSet.Config as cms

def HiEvtPlaneFlatProducer(**kwargs):
  mod = cms.EDProducer('HiEvtPlaneFlatProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
