import FWCore.ParameterSet.Config as cms

def CandIsoDumper(*args, **kwargs):
  mod = cms.EDAnalyzer('CandIsoDumper',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
