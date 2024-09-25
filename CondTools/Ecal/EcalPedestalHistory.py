import FWCore.ParameterSet.Config as cms

def EcalPedestalHistory(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalPedestalHistory',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
