import FWCore.ParameterSet.Config as cms

def CTPPSAcceptancePlotter(**kwargs):
  mod = cms.EDAnalyzer('CTPPSAcceptancePlotter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
