import FWCore.ParameterSet.Config as cms

def L1HOTreeProducer(*args, **kwargs):
  mod = cms.EDAnalyzer('L1HOTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
