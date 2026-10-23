import FWCore.ParameterSet.Config as cms

def PFCand_AssoMap(*args, **kwargs):
  mod = cms.EDProducer('PFCand_AssoMap',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
