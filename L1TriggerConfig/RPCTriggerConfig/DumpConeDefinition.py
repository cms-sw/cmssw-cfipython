import FWCore.ParameterSet.Config as cms

def DumpConeDefinition(**kwargs):
  mod = cms.EDAnalyzer('DumpConeDefinition',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
