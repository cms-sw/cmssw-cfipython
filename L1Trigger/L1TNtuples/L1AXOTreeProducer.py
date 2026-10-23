import FWCore.ParameterSet.Config as cms

def L1AXOTreeProducer(*args, **kwargs):
  mod = cms.EDAnalyzer('L1AXOTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
