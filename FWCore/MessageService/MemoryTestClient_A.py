import FWCore.ParameterSet.Config as cms

def MemoryTestClient_A(**kwargs):
  mod = cms.EDAnalyzer('MemoryTestClient_A',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
