import FWCore.ParameterSet.Config as cms

def L1EventTreeProducer(*args, **kwargs):
  mod = cms.EDAnalyzer('L1EventTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
