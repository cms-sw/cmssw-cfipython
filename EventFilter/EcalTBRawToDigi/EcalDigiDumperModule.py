import FWCore.ParameterSet.Config as cms

def EcalDigiDumperModule(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalDigiDumperModule',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
