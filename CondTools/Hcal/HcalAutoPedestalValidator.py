import FWCore.ParameterSet.Config as cms

def HcalAutoPedestalValidator(**kwargs):
  mod = cms.EDAnalyzer('HcalAutoPedestalValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
