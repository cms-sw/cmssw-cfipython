import FWCore.ParameterSet.Config as cms

def PUDumper(*args, **kwargs):
  mod = cms.EDAnalyzer('PUDumper',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
