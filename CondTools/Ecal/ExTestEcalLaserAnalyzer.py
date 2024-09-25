import FWCore.ParameterSet.Config as cms

def ExTestEcalLaserAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalLaserAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
