import FWCore.ParameterSet.Config as cms

def KineExample(**kwargs):
  mod = cms.EDAnalyzer('KineExample',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
