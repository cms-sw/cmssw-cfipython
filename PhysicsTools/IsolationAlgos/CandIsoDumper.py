import FWCore.ParameterSet.Config as cms

def CandIsoDumper(**kwargs):
  mod = cms.EDAnalyzer('CandIsoDumper',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
