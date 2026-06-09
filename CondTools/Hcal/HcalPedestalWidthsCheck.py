import FWCore.ParameterSet.Config as cms

def HcalPedestalWidthsCheck(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalPedestalWidthsCheck',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
