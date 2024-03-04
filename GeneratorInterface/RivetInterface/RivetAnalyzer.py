import FWCore.ParameterSet.Config as cms

def RivetAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('RivetAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
