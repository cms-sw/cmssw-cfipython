import FWCore.ParameterSet.Config as cms

def BoostedJetMerger(*args, **kwargs):
  mod = cms.EDProducer('BoostedJetMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
