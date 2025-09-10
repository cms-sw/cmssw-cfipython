import FWCore.ParameterSet.Config as cms

def PatJPsiProducer(*args, **kwargs):
  mod = cms.EDProducer('PatJPsiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
