import FWCore.ParameterSet.Config as cms

def EcalPnGraphDumperModule(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalPnGraphDumperModule',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
