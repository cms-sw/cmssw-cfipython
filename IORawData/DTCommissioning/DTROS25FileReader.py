import FWCore.ParameterSet.Config as cms

def DTROS25FileReader(*args, **kwargs):
  mod = cms.EDProducer('DTROS25FileReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
