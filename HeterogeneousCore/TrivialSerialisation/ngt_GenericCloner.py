import FWCore.ParameterSet.Config as cms

def ngt_GenericCloner(*args, **kwargs):
  mod = cms.EDProducer('ngt::GenericCloner',
    eventProducts = cms.vstring(),
    verbose = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
