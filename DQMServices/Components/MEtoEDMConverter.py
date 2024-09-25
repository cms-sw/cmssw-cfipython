import FWCore.ParameterSet.Config as cms

def MEtoEDMConverter(*args, **kwargs):
  mod = cms.EDProducer('MEtoEDMConverter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
