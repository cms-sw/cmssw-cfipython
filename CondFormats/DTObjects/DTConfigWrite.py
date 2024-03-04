import FWCore.ParameterSet.Config as cms

def DTConfigWrite(**kwargs):
  mod = cms.EDAnalyzer('DTConfigWrite',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
