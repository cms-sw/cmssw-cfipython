import FWCore.ParameterSet.Config as cms

def PVSSIDReader(**kwargs):
  mod = cms.EDAnalyzer('PVSSIDReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
