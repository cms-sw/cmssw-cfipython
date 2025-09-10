import FWCore.ParameterSet.Config as cms

def HcalAutoPedestalValidator(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalAutoPedestalValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
