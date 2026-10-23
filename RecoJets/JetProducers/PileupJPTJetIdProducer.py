import FWCore.ParameterSet.Config as cms

def PileupJPTJetIdProducer(*args, **kwargs):
  mod = cms.EDProducer('PileupJPTJetIdProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
