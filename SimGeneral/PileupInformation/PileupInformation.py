import FWCore.ParameterSet.Config as cms

def PileupInformation(*args, **kwargs):
  mod = cms.EDProducer('PileupInformation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
