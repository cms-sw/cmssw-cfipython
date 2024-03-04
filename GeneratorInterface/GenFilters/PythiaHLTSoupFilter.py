import FWCore.ParameterSet.Config as cms

def PythiaHLTSoupFilter(**kwargs):
  mod = cms.EDFilter('PythiaHLTSoupFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
