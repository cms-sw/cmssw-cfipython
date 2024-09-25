import FWCore.ParameterSet.Config as cms

def JetCoreClusterSplitter(*args, **kwargs):
  mod = cms.EDProducer('JetCoreClusterSplitter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
