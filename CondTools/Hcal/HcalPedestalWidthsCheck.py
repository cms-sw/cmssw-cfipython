import FWCore.ParameterSet.Config as cms

def HcalPedestalWidthsCheck(**kwargs):
  mod = cms.EDAnalyzer('HcalPedestalWidthsCheck',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
