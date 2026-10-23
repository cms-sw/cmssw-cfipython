import FWCore.ParameterSet.Config as cms

def EcalSCDynamicDPhiParametersMaker(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalSCDynamicDPhiParametersMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
