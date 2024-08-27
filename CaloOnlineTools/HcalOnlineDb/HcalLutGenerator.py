import FWCore.ParameterSet.Config as cms

def HcalLutGenerator(**kwargs):
  mod = cms.EDAnalyzer('HcalLutGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
