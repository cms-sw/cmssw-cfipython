import FWCore.ParameterSet.Config as cms

def ValidateRadial(**kwargs):
  mod = cms.EDAnalyzer('ValidateRadial',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
