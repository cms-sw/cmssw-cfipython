import FWCore.ParameterSet.Config as cms

def DeDxHitInfoProducer(**kwargs):
  mod = cms.EDProducer('DeDxHitInfoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
