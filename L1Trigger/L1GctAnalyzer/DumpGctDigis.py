import FWCore.ParameterSet.Config as cms

def DumpGctDigis(**kwargs):
  mod = cms.EDAnalyzer('DumpGctDigis',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
