import FWCore.ParameterSet.Config as cms

def EcalDCCHeaderDumperModule(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalDCCHeaderDumperModule',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
