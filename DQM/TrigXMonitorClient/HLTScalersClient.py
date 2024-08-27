import FWCore.ParameterSet.Config as cms

def HLTScalersClient(**kwargs):
  mod = cms.EDAnalyzer('HLTScalersClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
