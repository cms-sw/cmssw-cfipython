import FWCore.ParameterSet.Config as cms

def PyquenGeneratorFilter(**kwargs):
  mod = cms.EDFilter('PyquenGeneratorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
