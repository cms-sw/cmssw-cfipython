import FWCore.ParameterSet.Config as cms

def JetCoreClusterSplitter(**kwargs):
  mod = cms.EDProducer('JetCoreClusterSplitter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
