import FWCore.ParameterSet.Config as cms

def HcalDigitizerTest(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalDigitizerTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
