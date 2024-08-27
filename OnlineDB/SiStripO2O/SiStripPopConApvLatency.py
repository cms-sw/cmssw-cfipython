import FWCore.ParameterSet.Config as cms

def SiStripPopConApvLatency(**kwargs):
  mod = cms.EDAnalyzer('SiStripPopConApvLatency',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
