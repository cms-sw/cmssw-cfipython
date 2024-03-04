import FWCore.ParameterSet.Config as cms

def DumpBtagTable(**kwargs):
  mod = cms.EDAnalyzer('DumpBtagTable',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
