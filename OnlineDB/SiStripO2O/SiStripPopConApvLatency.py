import FWCore.ParameterSet.Config as cms

def SiStripPopConApvLatency(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripPopConApvLatency',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
