import FWCore.ParameterSet.Config as cms

def DumpScObjects(**kwargs):
  mod = cms.EDAnalyzer('DumpScObjects',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
