import FWCore.ParameterSet.Config as cms

def JPTJetIdSelector(*args, **kwargs):
  mod = cms.EDProducer('JPTJetIdSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
