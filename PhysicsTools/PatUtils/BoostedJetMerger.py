import FWCore.ParameterSet.Config as cms

def BoostedJetMerger(**kwargs):
  mod = cms.EDProducer('BoostedJetMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
