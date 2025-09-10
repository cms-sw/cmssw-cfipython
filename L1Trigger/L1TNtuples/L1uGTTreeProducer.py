import FWCore.ParameterSet.Config as cms

def L1uGTTreeProducer(*args, **kwargs):
  mod = cms.EDAnalyzer('L1uGTTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
