import FWCore.ParameterSet.Config as cms

def PatJPsiProducer(**kwargs):
  mod = cms.EDProducer('PatJPsiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
