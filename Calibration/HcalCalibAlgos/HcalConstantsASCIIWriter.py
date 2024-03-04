import FWCore.ParameterSet.Config as cms

def HcalConstantsASCIIWriter(**kwargs):
  mod = cms.EDAnalyzer('HcalConstantsASCIIWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
