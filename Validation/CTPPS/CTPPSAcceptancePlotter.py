import FWCore.ParameterSet.Config as cms

def CTPPSAcceptancePlotter(*args, **kwargs):
  mod = cms.EDAnalyzer('CTPPSAcceptancePlotter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
