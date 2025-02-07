import FWCore.ParameterSet.Config as cms

def HcalConstantsASCIIWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalConstantsASCIIWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
