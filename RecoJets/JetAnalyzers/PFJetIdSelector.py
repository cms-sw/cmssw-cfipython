import FWCore.ParameterSet.Config as cms

def PFJetIdSelector(*args, **kwargs):
  mod = cms.EDProducer('PFJetIdSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
