import FWCore.ParameterSet.Config as cms

def RivetAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('RivetAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
