import FWCore.ParameterSet.Config as cms

def ShallowTree(**kwargs):
  mod = cms.EDAnalyzer('ShallowTree',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
