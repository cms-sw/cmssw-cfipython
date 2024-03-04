import FWCore.ParameterSet.Config as cms

def DTKeyedConfigDBInit(**kwargs):
  mod = cms.EDAnalyzer('DTKeyedConfigDBInit',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
