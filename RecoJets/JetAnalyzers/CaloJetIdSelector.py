import FWCore.ParameterSet.Config as cms

def CaloJetIdSelector(*args, **kwargs):
  mod = cms.EDProducer('CaloJetIdSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
